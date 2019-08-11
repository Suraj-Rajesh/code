#!/bin/python
import os
import pwd
import grp
import sys
import time
import errno
import fcntl
import string
import shutil
import random
import logging
import tarfile
import argparse
import contextlib
from subprocess import Popen, PIPE

#
# When this is called as a process(subprocess.Popen()) in other components
# PYTHONPATH is not updated for appliance imports in
# the process context that we create, thus failing below imports. Hence,
# updating PYTHONPATH to counter these scenarios
#
sys.path.append('/path/update/goes/here')

SAMPLE_LOG = '/var/log/sample.log'
log_handler = logging.FileHandler(SAMPLE_LOG)
log_format = logging.Formatter('[%(asctime)s] (%(name)s.%(funcName)s:'
                               '%(lineno)d) %(levelname)s - %(message)s',
                               '%m-%d %H:%M:%S')
log_handler.setFormatter(log_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

#
# exit codes
#
SUCCESS_EXIT            = 0
PARSE_FAILURE_EXIT      = 3
CMD_FAILURE_EXIT        = 4


#
# exceptions
#
class LockAcquisitionError(Exception):
    pass


class LockTimeoutExceeded(Exception):
    pass


class CmdExecError(Exception):
    pass


def random_str():
    return ''.join(random.choice(string.lowercase) for i in
            range(random.randint(7, 9)))


@contextlib.contextmanager
def lock(dir_name, lock_file, timeout=10*60):
    try:
        try:
            lock_acquired = False
            lfile_path = '{}/{}'.format(dir_name, lock_file)
            start_time = time.time()
            fp = open(lfile_path, 'w+')
        except Exception as exc:
            logmsg = 'Error opening lockfile: {}'.format(exc)
            logger.error(logmsg)
            raise LockAcquisitionError(logmsg)

        while True:
            try:
                fcntl.flock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
                lock_acquired = True
                yield
                break
            except IOError as exc:
                #
                # if lock acquisition fails due to another process holding it,
                # errno EAGAIN is raised(which is expected when multiple
                # processes are vying for the lock), in which case, continue
                # waiting for lock until timeout. Otherwise, its an unexpected
                # IOError, raise that Exception
                #
                if exc.errno != errno.EAGAIN:
                    logmsg = 'IO Error during lock acq: {}'.format(exc)
                    logger.error(logmsg)
                    raise LockAcquisitionError(logmsg)
                else:
                    if timeout is not None and \
                    time.time() > (start_time + timeout):
                        logmsg = 'lock acquisition timeout exceeded'
                        logger.error(logmsg)
                        raise LockTimeoutExceeded(logmsg)
                    else:
                        time.sleep(1)
    except Exception as exc:
        raise
    finally:
        if lock_acquired:
            fcntl.flock(fp, fcntl.LOCK_UN)
            fp.close()


def create_recovery_archive(category):
    try:
        archive = '/path/to/archive'
        content_list = ['list of files to be archived']
        with tarfile.open(archive, 'w:gz') as t:
            for c in content_list:
                t.add(c)
    except Exception as exc:
        logmsg = ('Recovery creation failure for category: '
                 '{}: {}'.format(category, exc))
        logger.error(logmsg)
        raise RecoveryCreationError(logmsg)


def recover(category):
    try:
        archive = 'path/to/archive'
        tmp_rec = 'path/to/tmp/recovery/file'
        content = ['list of files to be recovered back from archive']

        shutil.rmtree(tmp_rec) if os.path.isdir(tmp_rec) else None
        os.unlink(tmp_rec) if os.path.isfile(tmp_rec) else None

        tf = tarfile.open(archive)
        tf.extractall(tmp_rec)

        if category == 'simple':
            for dst in content:
                recovered = '{}{}'.format(tmp_rec, dst)
                shutil.copy2(recovered, dst)
        else:
            for dst in content:
                recovered = '{}{}'.format(tmp_rec, dst)
                shutil.rmtree(dst) if os.path.isdir(dst) else None
                os.unlink(dst) if os.path.isfile(dst) else None
                shutil.move(recovered, dst)
    except Exception as exc:
        logmsg = 'Recovery failure for category {}'.format(category)
        logger.error(exc)
        raise RecoveryError(logmsg)
    finally:
        shutil.rmtree(tmp_rec) if os.path.isdir(tmp_rec) else None


def check(category):
    lock_file = '.{}.lock'.format(cmmd_category)
    try:
        with lock(DB_DIR, lock_file):
            my_func()
    except LockTimeoutExceeded:
        logger.error('lock acq failed')
    except Exception:
        m = 'Validation failed'
        logger.error(m)
        raise


def update_file(tmp_file):
    try:
        uid = pwd.getpwnam(SCRIPT_USER).pw_uid
        gid = grp.getgrnam(SCRIPT_USER).gr_gid
        os.chown(tmp_file, uid, gid)
        os.chmod(tmp_file, PERMS)
        shutil.copy2(tmp_file, CONFIG)
    except Exception as exc:
        msg = 'Error updating file: {}'.format(exc)
        raise UpdateFailure(msg)


def copy_file(dst_file):
    backup = '{}.backup'.format(dst_file)

    # remove any files/dirs of same name if already present
    os.remove(dst_file) if os.path.isfile(dst_file) else None
    shutil.rmtree(dst_file) if os.path.isdir(dst_file) else None
    os.remove(backup) if os.path.isfile(backup) else None
    shutil.rmtree(backup) if os.path.isdir(backup) else None
    shutil.copy2(CONFIG, dst_file)
    shutil.copy2(CONFIG, backup)
    return backup


def delete_lines(tmp_crontab, script):
    with open(tmp_crontab, 'r+') as fp:
        content = fp.readlines()
        fp.seek(0)
        for line in content:
            if script not in line:
                fp.write(line)
        fp.truncate()


def cmd_exec(cmd, args_list, err_to_stdout=False):
    # sanitize cmd list to not have secure info like password while logging
    nolog_args = ['-p', '--password', '-c', '--cur_password']
    log_cmd_list = [cmd] + args_list
    for arg in nolog_args:
        if arg in log_cmd_list:
            rep_index = log_cmd_list.index(arg) + 1
            try:
                log_cmd_list[rep_index] = '****'
            except IndexError:
                pass
    use_stdin = False

    # Check for read from stdin
    for arg in log_cmd_list:
        if arg == '--stdin':
            use_stdin = True
            break

    lock_file = '.{}.lock'.format(ETC)
    try:
        logger.info('Attempting cmd execution of {}'.format(cmd))
        with lock(AIDEDB_DIR, lock_file):
            cmd_list = [cmd] + args_list
            proc = Popen(cmd_list, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            if use_stdin:
                # keeping passwords out of logs
                _, err = proc.communicate(sys.stdin.read().encode())
            else:
                _, err = proc.communicate()

        rc = proc.returncode
        if rc:
            if err_to_stdout:
                sys.stderr.write(err)
            logger.error('{} failed:({}) {}'.format(log_cmd_list, rc, err))
        else:
            logger.info('cmd {} succeeded'.format(log_cmd_list))

        return rc
    except LockTimeoutExceeded:
        logger.error('lock acq timeout for cmd: {}'.format(log_cmd_list))
        raise CmdExecError('{} execution failed'.format(log_cmd_list))
    except InitializationError:
        logger.error('{}: re-init on etc category failed'.format(log_cmd_list))
        raise CmdExecError('{} execution failed'.format(log_cmd_list))
    except Exception as exc:
        logger.error('Execution of {} failed: {}'.format(log_cmd_list, exc))
        logger.exception(exc)
        raise CmdExecError('{} execution failed'.format(log_cmd_list))


def arg_parser():
    try:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--init', action='store', metavar='[all options supported]')
        group.add_argument('--enable', action='store', metavar='[all options supported]')
        group.add_argument('--ctrl', nargs=argparse.REMAINDER, metavar='args to ctrl')

        return parser.parse_args()
    except Exception as exc:
        logger.exception(exc)
        raise ParseError('Error parsing')


if __name__ == '__main__':
    try:
        args = arg_parser()

        if args.init:
            init(args.init)
        elif args.enable:
            my_enable_fn()
        elif args.ctrl:
            rc = cmd_exec(CMD, args.ctrl, err_to_stdout=True)
            exit(rc)
    except ParseError:
        exit(PARSE_FAILURE_EXIT)
    except CmdExecError:
        exit(CMD_FAILURE_EXIT)
    except Exception as exc:
        exit(FAILURE_EXIT)
    else:
        exit(SUCCESS_EXIT)
