#include <stdlib.h>
#include <string.h>

#include "logs.h"

int g_log_level = LOG_INFO;         /* definition of global log level */
static char *log_file = NULL;       /* log file */


/****************************************************************************
 *
 *  filename: specify log file to write logs to
 *
 *  log_level: Set to one of the below log levels
 *              - LOG_NONE
 *              - LOG_ERROR
 *              - LOG_WARNING
 *              - LOG_INFO
 *              - LOG_DEBUG
 *
 ***************************************************************************/
void
init_logging(char * filename, int log_level){
    log_file = strdup(filename);
    g_log_level = log_level;
}

char *
log_format(char *format, ...){
    char buffer[BUFSIZ] = {0};
    va_list args_ptr;

    va_start(args_ptr, format);
    vsnprintf(buffer, sizeof(buffer), format, args_ptr);
    va_end(args_ptr);

//    buffer[sizeof(buffer) - 1] = 0;
    return strdup(buffer);
}

void
logger(int log_level, char *date, char *time, char *filename, char *function,
       int line_no, char *errno_msg, char *log_msg){

    FILE    *fptr = NULL;
    char    *log_type = NULL;
    char    buffer[BUFSIZ];

    /* get specified log level */
    switch(log_level){
        case LOG_DEBUG:
            log_type = "DEBUG";
            break;
        case LOG_INFO:
            log_type = "INFO";
            break;
        case LOG_WARNING:
            log_type = "WARNING";
            break;
        case LOG_ERROR:
            log_type = "ERROR";
            break;
        default:
            log_type = "UNKNOWN";
            break; 
    }

    /* if no errno message */
    if (0 == strcmp(errno_msg, "None")){ 
        snprintf(buffer, BUFSIZ, "%s %s [%s] (%s:%s:%d) %s\n",
                date, time, log_type, filename, function, line_no,
                log_msg);
    }
    else { 
        snprintf(buffer, BUFSIZ, "%s %s [%s] (%s:%s:%d errno: %s) %s\n",
                date, time, log_type, filename, function, line_no,
                errno_msg, log_msg);
    }

    /* check if log file set */
    if (log_file){
        fptr = fopen(log_file, "a");

        if (fptr){            
            fprintf(fptr, "%s", buffer);
            fflush(fptr);
            fclose(fptr);
        }
        else { fprintf(stderr, "Error opening log file\n"); }
    }
    else { fprintf(stdout, "Logging not initialized\n"); }

    free(log_msg);
}
