#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdarg.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TIMEOUT 100

int CMD_TIMED_OUT = 0;
int CHILD_DONE = 0;

void child_handler(int sig) {
    CHILD_DONE = 1;
}

void alarm_handler(int sig) {
    CMD_TIMED_OUT = 1;
}

int
run_cmd_timeout(char *cmdstr, int count, int timeout) {
    pid_t pid = 0;
    int index = 0;
    int final_rc = 0;
    int child_state = 0;
    char * token = NULL;

    /* array of string pointers to hold cmd */
    char **cmd_array = malloc(sizeof(char *) * (count + 1));
    if (cmd_array == NULL) {
        final_rc = 1;
        goto end;
    }

    for (index = 0; index < count + 1; index++) {
        cmd_array[index] = NULL;
    }

    /* this is a sacrificial string, since strtok modifies string during
    * tokenization and we want to keep the passed cmd string as it is */
    char * cmd_parse_str = (char *)malloc(sizeof(char) * 256);
    if (cmd_parse_str == NULL) {
        final_rc = 1;
        goto end;
    }

    memset(cmd_parse_str, 0, 256);
    strcpy(cmd_parse_str, cmdstr);
    cmd_parse_str[255] = '\0';

    /* tokenize and create command array */
    token = strtok(cmd_parse_str," ");
    for (index = 0; token != NULL; index++) {
        cmd_array[index] = (char *)malloc(sizeof(char) * 256);
        if (cmd_array[index] == NULL) {
            final_rc = 1;
            goto end;
        }
        strcpy(cmd_array[index], token);
        token = strtok (NULL, " ");
    }

    cmd_array[index] = NULL;

    /* fork */
    pid = fork();
    if (pid == -1) {
        final_rc = 2;
        goto end;
    } else if (pid == 0) {
        /* execute cmd as a child process here */
        execvp(cmd_array[0], cmd_array);
        exit(1);
    }

    /* set up the signal handlers after forking so the child doesn't inherit them */
    signal(SIGALRM, alarm_handler);
    signal(SIGCHLD, child_handler);

    /* start alarm */
    alarm(timeout);

    /* wait until a signal is received */
    pause();

    if (CMD_TIMED_OUT) {
        child_state = waitpid(pid, NULL, WNOHANG);
        if (child_state == 0) {
            /* child still running, kill it */
            printf("child running, kill it\n");
            kill(pid, SIGKILL);
            wait(NULL);
        } else {
            printf("alarm triggered, but child finished normally\n");
        }
    } else if (CHILD_DONE) {
        printf("process finished in time\n");
        wait(NULL);
    } else {
        printf("Some other signal caught\n");
        wait(NULL);
    }

end:
  for (index = 0; index <= count; index++) {
      if (cmd_array[index]) {
          free(cmd_array[index]);
      }
  }

  if (cmd_parse_str) {
      free(cmd_parse_str);
  }

  if (cmd_array) {
      free(cmd_array);
  }

  return final_rc;
}

int
main() {
    char cmdstr[1024] = {0};
    sprintf(cmdstr, "%s %s", "/home/suraj/r.out", "two");
    run_cmd_timeout(cmdstr, 2, TIMEOUT);
}
