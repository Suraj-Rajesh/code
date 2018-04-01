#ifndef __LOGS_H__
#define __LOGS_H__

/* required standard includes for this header file */
#include <errno.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

/* log levels */
#define LOG_NONE        0
#define LOG_ERROR       1
#define LOG_WARNING     2
#define LOG_INFO        3
#define LOG_DEBUG       4

/* declaration of global log level */
extern int g_log_level;

/* logging functions */
void init_logging(char *filename, int log_level);
char *log_format(char *format, ...);
void logger(int log_level, char *date, char *time, char *filename, 
        char *function, int line_no, char *errno_msg, char *log_msg);

#define clean_errno()   ((0 == errno) ? "None" : strerror(errno))

#define DERROR(...)    if (g_log_level >= LOG_ERROR) {\
    logger(LOG_ERROR, __DATE__, __TIME__, __FILE__, (char *)__func__,\
            __LINE__, clean_errno(), log_format(__VA_ARGS__)); }

#define DWARN(...)    if (g_log_level >= LOG_WARNING) {\
    logger(LOG_WARNING, __DATE__, __TIME__, __FILE__, (char *)__func__,\
            __LINE__, clean_errno(), log_format(__VA_ARGS__)); }

#define DINFO(...)    if (g_log_level >= LOG_INFO) {\
    logger(LOG_INFO, __DATE__, __TIME__, __FILE__, (char *)__func__,\
            __LINE__, clean_errno(), log_format(__VA_ARGS__)); }

#define DDEBUG(...)    if (g_log_level >= LOG_DEBUG) {\
    logger(LOG_DEBUG, __DATE__, __TIME__, __FILE__, (char *)__func__,\
            __LINE__, "None", log_format(__VA_ARGS__)); }

#define ERRMSG(...) { fprintf(stderr, __VA_ARGS__); fprintf(stderr, "\n");\
                      DERROR(__VA_ARGS__); }

#define INFOMSG(...) { fprintf(stdout, __VA_ARGS__); fprintf(stdout, "\n");\
                      DINFO(__VA_ARGS__); }

#define check(condition, ...) if (!(condition)) {\
    DERROR(__VA_ARGS__); goto error; }

#endif
