/*

Run as, ./a.out <child runtime> <timeout>

For example,

./a.out 5 3 - this makes child run for 5 seconds, but since timeout is only 3, child will be killed.
./a.out 5 10 - here child runtime is lesser than timeout, so child executes and exits normally.

*/

#include <stdio.h>
#include <sys/wait.h>
#include <time.h>
#include <errno.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>


// poll_interval in seconds and is optional. Pass 0 to use default.
#define HT_WAIT_FOR_CHILD_POLL_INTERVAL 1

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
        poll_interval = HT_WAIT_FOR_CHILD_POLL_INTERVAL;
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
            }
            else {
                printf("child did not exit normally - %d\n", status);
                ret = status;
            }
            break;
        }

        // if it is ERROR, get out
        if( -1 == wait_ret && EINTR != errno )
        {
            ret = errno;
            printf("waitpid failed - errno=%d\n", ret);
            break;
        }

        // check if wait has timed out
        elapsed_time = time(NULL) - start_time;
        if( elapsed_time > timeout_seconds )
        {
            printf("waiting for child timeout. Killing child %d\n", pid);
            kill(pid, SIGKILL);
            ret = ETIMEDOUT;
            break;
        }

        sleep(poll_interval);

    } while( wait_ret <= 0 );

    return ret;
}

static int hcutils_parse_args(char *cmdline, char **argv, int argv_count)
{
    int   nArgCount = 0 ;

    while( nArgCount < argv_count && cmdline && '\0' != *cmdline )
    {
        // skip leading white spaces
        while( ' ' == *cmdline)
            cmdline++;
        if( '\0' == *cmdline )
            break;

        if( '"' == *cmdline )
        {
            char *end ;
            cmdline++;
            end = strchr(cmdline, '"');
            if( !end )
                break;
            *end++ = '\0';
            // next character can be space or terminating '\0'
            if( '\0' != *end )
                *end++ = '\0';
            argv[nArgCount++] = cmdline;
            cmdline = end;
        }
        else
        {
            char *token = strchr(cmdline, ' ');
            if( token )
            {
                *token++ = '\0';
                argv[nArgCount++] = cmdline;
                cmdline = token;
            }
            else
            {
                argv[nArgCount++] = cmdline;
                cmdline = NULL;
            }
        }
    }

    // there could be trailing spaces but arg_count reached
    if( cmdline )
    {
        while( ' ' == *cmdline )
            cmdline++;
    }

    // check if we have parsed the command line fully
    if( cmdline && '\0' != *cmdline )
        return -1;  // incomplete parsing

    return nArgCount;
}

#define HT_EXEC_MAX_ARGS 100
//
// hcutils_exec does not support stdout/stderr redirection
// returns
// 0 - success; the *cmdret has the child program return value
// 127 - failed to execute child program
// any other value - failure
//
int
ht_exec(
    /* in */ const char *cmd_str,
    /* out */ int *cmd_ret,
    /* in */ int timeout_sec) {
    pid_t   pid;
    int     ret;
    int     status;
    pid_t   wait_ret;
    int     arg_count;
    char    *cmdbuf;
    char    *argv[HT_EXEC_MAX_ARGS];

    cmdbuf = strdup(cmd_str);
    if( !cmdbuf )
        return ENOMEM;

    arg_count = hcutils_parse_args(cmdbuf, argv, HT_EXEC_MAX_ARGS-1);
    if( arg_count <= 0 )
    {
        ret = EINVAL;
        goto end;
    }
    argv[arg_count] = NULL;

    pid = fork();
    if(-1 == pid) {
        ret = errno;
        goto end;
    }

    if(0 == pid) {
        /* exec child here */
        execv(argv[0], argv);
        printf("execv of %s failed - %d\n", cmd_str, errno);
        _exit(127);
    }

    // parent process
    ret = wait_for_child(pid, timeout_sec, 0, cmd_ret);

end:
    free(cmdbuf);
    return ret;
}


int main(int argc, char **argv)
{
    int child_ret;
    int ret ;
    char cmdline[512];
    int wait;

    if(argc == 2) {
        wait = atoi(argv[1]);
        // child process
        printf("This is child process - pid=%d\n", getpid());
        //getchar();
        printf("Child waiting for %d seconds\n", wait);
        sleep(wait);
        printf("Exiting child - pid=%d\n", getpid());
        return 99;
    }

    if(argc != 3) {
        printf("invalid param\n");
        return -1;
    }

    sprintf(cmdline, "%s %d", argv[0], atoi(argv[1]));

    wait = atoi(argv[2]);
    printf("Parent (%d) - child timeout %d seconds\n", getpid(), wait);
    ret = ht_exec(cmdline, &child_ret, wait);
    printf("ht_exec - ret=%d, child_ret=%d\n", ret, child_ret);
    return ret;
}
