#include <stdio.h>

int main(void){
    int number, revnum = 0;

    printf("Enter: ");
    scanf("%d", &number);

    while (number != 0){
        revnum = revnum*10 + number%10;
        number/=10;
    }

    printf("Rev: %d\n", revnum);
    return 0;
}
