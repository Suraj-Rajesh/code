from subprocess import Popen, PIPE
from collections import namedtuple
from functools import wraps
from sys import exit


ProcessInfo = namedtuple('process_info', ['return_code', 'stdout', 'stderr'])

# setup logging
import logging
logger = logging.getLogger(__name__)

log_handler = logging.FileHandler('/var/log/access_control.log')
log_formatter = logging.Formatter('[%(asctime)s] (%(name)s.%(funcName)s:\
%(lineno)d) %(levelname)s - %(message)s', '%m-%d %H:%M:%S')
log_handler.setFormatter(log_formatter)

logger.setLevel(logging.INFO)
logger.addHandler(log_handler)


def dequote_string(st):
    """Removes a string enclosed in quotes"""
    if len(st) > 2 and st.startswith(("'", '"')) and st[0] == st[-1]:
        return st[1:-1]
    return st


# meta-decorator for process function
# process._original(args) : execute function 'process' only, without decorator
# process(args) : execute function 'process' with decoration
def include_original(decorator):
    def decorator_wrapper(func):
        decorated = decorator(func)
        decorated._original = func
        return decorated
    return decorator_wrapper


@include_original
def proc_handler(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        try:
            cmd = args[0].split()[0]
            # only passed values can be captured, not default values
            # for default values, use function introspection
            dep = kwargs['dependency'] if 'dependency' in kwargs else None
            return func(*args, **kwargs)
        except OSError as error:
            if 2 == error.errno:
                msg = '\'%s\' not found.' % cmd
                if dep:
                    msg += ' Please install \'%s\'.' % dep
                logger.error(msg)
                print msg
                exit(1)
            else:
                msg = '%s: %s' % (cmd, error)
                logger.error(error)
                print msg
                exit(1)
        except Exception as error:
            msg = '%s: %s' % (cmd, error)
            logger.error(error)
            print msg
            exit(1)

    return func_wrapper


@proc_handler
def process(command,
            outfile=None,
            appendfile=None,
            dequote=False,
            shell=False,
            dependency=None,
            cwd=None):
    """Spawns a new process

    Runs command provided as a new process and returns process info

    Args:
        command (str): Command to be executed
        outfile (Optional[str]): file to write command output to
        appendfile (Optional[str]): file to append command output to
        dequote(Optional[bool]): remove extra escaped quotes in commands. Popen
            doesn't play well with some commands containing quotes. Need to
            dequote then.
        shell (Optional[bool]): run process in the shell
        dependency (Optional[str]): dependency needed for command to be run.
        Displays error message to install the dependency for command to run.
        cwd (Optional[str]): working directory to switch to, to run a
        particular command.

    Returns:
        ProcessInfo: (return code, stdout, stderr)

    """

    if not shell:
        if dequote:
            command = [dequote_string(arg) for arg in command.split()]
        else:
            command = command.split()

    if outfile or appendfile:
        if outfile:
            mode = 'wb'
            open_file = outfile
        else:
            mode = 'ab'
            open_file = appendfile

        with open(open_file, mode) as outfp:
            proc = Popen(command,
                         stdout=outfp,
                         stderr=PIPE,
                         shell=shell,
                         cwd=cwd)
            out, err = proc.communicate()
    else:
        proc = Popen(command,
                     stdout=PIPE,
                     stderr=PIPE,
                     shell=shell,
                     cwd=cwd)
        out, err = proc.communicate()

    return ProcessInfo(proc.returncode, out, err)
