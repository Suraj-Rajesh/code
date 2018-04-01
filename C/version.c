#include <stdio.h>

#define VERSION "2.0"

int 
main(void)
{
    char * request = NULL;

    request = "/" VERSION "/keyid_getkey/";
    printf("%s\n", request);

    return 0;
}
