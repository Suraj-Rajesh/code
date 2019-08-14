/* This forks a child process, waits for timeout period. If child still running after timeout, kill it */

#include <stdio.h>
#include <sys/wait.h>
#include <time.h>
#include <errno.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

/* poll_interval in seconds and is optional. Pass 0 to use default. */
#define WAIT_FOR_CHILD_POLL_INTERVAL 1

int
wait_for_child(pid_t pid, int timeout_seconds, int poll_interval, int *child_ret)
{
    int    ret;
    int    status;
    int    wait_ret;
    time_t start_time;
    time_t elapsed_time;

    *child_ret = -1;

    if(0 == poll_interval) {
        poll_interval = WAIT_FOR_CHILD_POLL_INTERVAL;
    }

    time(&start_time);

    do
    {
        wait_ret = waitpid(pid, &status, WNOHANG);
        /* child is done */
        if(wait_ret == pid) {
            /* child exited normally */
            if(WIFEXITED(status)) {
                *child_ret = WEXITSTATUS(status);
                ret = 0;
            } else {
                printf("child did not exit normally - %d\n", status);
                ret = status;
            }
            break;
        }

        /* if errored out(not because of signal), log and get out */
        if(-1 == wait_ret && EINTR != errno) {
            ret = errno;
            printf("waitpid failed - errno=%d, %s\n", ret, strerror(errno));
            break;
        }

        /* check if wait timed out */
        elapsed_time = time(NULL) - start_time;
        if(elapsed_time > timeout_seconds) {
            printf("Waiting for child timeout. Killing child\n", pid);
            kill(pid, SIGKILL);
            ret = ETIMEDOUT;
            break;
        }

        sleep(poll_interval);

    } while(wait_ret == 0); /* poll till child changes state */

    return ret;
}


static int utils_parse_args(
        /* in */  char *cmdline,
        /* out */ char **argv,
        /* in */  int argv_count) {
    int   n_arg_count = 0 ;

    while(n_arg_count < argv_count && cmdline && '\0' != *cmdline) {
        /* skip leading white spaces */
        while(' ' == *cmdline) {
            cmdline++;
        }

        if('\0' == *cmdline) {
            break;
        }

        if( '"' == *cmdline ) {
            char *end ;
            cmdline++;

            end = strchr(cmdline, '"');
            if(!end) {
                break;
            }

            *end++ = '\0';
            /* next character can be space or terminating '\0' */
            if('\0' != *end) {
                *end++ = '\0';
            }

            argv[n_arg_count++] = cmdline;
            cmdline = end;
        } else {
            char *token = strchr(cmdline, ' ');
            if(token) {
                *token++ = '\0';
                argv[n_arg_count++] = cmdline;
                cmdline = token;
            } else {
                argv[n_arg_count++] = cmdline;
                cmdline = NULL;
            }
        }
    }

    /* there could be trailing spaces but arg_count reached */
    if(cmdline) {
        while(' ' == *cmdline) {
            cmdline++;
        }
    }

    /* check if we have parsed the command line fully */
    if(cmdline && '\0' != *cmdline) {
        /* incomplete parsing */
        return -1;
    }

    return n_arg_count;
}

#define HT_EXEC_MAX_ARGS    100

int
exec(
    /* in  */ const char *cmdstr,
    /* out */ int *cmd_ret,
    /* in  */ int timeout_sec) {
    pid_t   pid;
    int     ret;
    int     status;
    pid_t   wait_ret;
    int     arg_count;
    char    *cmdbuf;
    char    *argv[HT_EXEC_MAX_ARGS];

    cmdbuf = strdup(cmdstr);
    if(!cmdbuf) {
        return ENOMEM;
    }

    arg_count = utils_parse_args(cmdbuf, argv, HT_EXEC_MAX_ARGS - 1);
    if(arg_count <= 0) {
        ret = EINVAL;
        goto end;
    }
    argv[arg_count] = NULL;

    pid = fork();
    if(-1 == pid) {
        ret = errno;
        printf("Fork failed for: %s - errno=%d, %s", cmdstr,
                                                     errno,
                                                     strerror(errno));
        goto end;
    }

    if(0 == pid) {
        /* exec child here */
        execv(argv[0], argv);
        printf("execv of %s failed - errno=%d, %s\n", cmdstr,
                                                      errno,
                                                      strerror(errno));
        _exit(127);
    }

    /* parent process - wait for child here */
    ret = wait_for_child(pid, timeout_sec, 0, cmd_ret);

end:
    if (cmdbuf) {
        free(cmdbuf);
    }
    return ret;
}


int main(int argc, char **argv) {
    int rc = 0;
    char cmdstr[1024] = {0};
    sprintf(cmdstr, "%s %s", "/home/suraj/r.out", "two");
    int cmd_ret = 0;
    rc = exec(cmdstr,
              &cmd_ret,
              20);
    printf("CMDRET: %d\n", cmd_ret);
    if (rc) {
        printf("Error executing %s\n", cmdstr);
    }
    return 0;
}
