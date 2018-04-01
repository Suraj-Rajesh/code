#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Another way to define a macro: gcc -g quick_str.c -D QUICK_STRCMP */
#define QUICK_STRCMP
#define STRCMP(a, b)    ((*(a)) == (*(b))) ? \
		            	strcmp((a), (b)) : ((int)(*(a)) - (int)(*(b)))

int main(int argc, char * argv[]){
    int rc = 0;
    char * str1 = (char *)malloc(sizeof(char)*20);
    char * str2 = (char *)malloc(sizeof(char)*20);
    
    printf("s1:");
    scanf("%s", str1);
    printf("s2:");
    scanf("%s", str2);

#ifdef QUICK_STRCMP
    rc = STRCMP(str1, str2);
    printf("Returned: %d\n", rc);
#else
    rc = strcmp(str1, str2);
    printf("strcmp returned: %d\n", rc);
#endif

    free(str1);
    free(str2);
    return 0;
}
