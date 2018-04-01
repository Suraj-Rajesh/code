#include <stdio.h>
#include <string.h>

int main(void){
    char temp;
    char * start = NULL, * end = NULL;
    char str[100] = {0};

    printf("Enter: ");
    scanf("%s", str);

    for(start = str, end = str + strlen(str) - 1; start < end; start++, end--) {
        temp = *start;
        *start = *end;
        *end = temp;
    }
    printf("Reversed: %s\n", str);
    return 0;
}
