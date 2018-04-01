#include <string.h>

#include "demon.h"
#include "logs.h"

int
main(int argc, char *argv[]){
    init_logging("demon.log", LOG_DEBUG);
    DINFO("Starting main");
    DINFO("Checking variable args %d : %s", 1, "test 1");
    INFOMSG("On-flight started");

    check(1 != 1, "Check test !!");

    return 0;

error:
    return 0;
}
