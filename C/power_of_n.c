#include <stdio.h>

int power_of_n(int x, int n){
    // Check for special case if power is 0
    if (n == 0) return 1;
    // Condition check
    if (n == 1) return x;
    // Recursion
    // printf("Hit\n");
    int one_half = power_of_n(x, n/2);
    return one_half * one_half;
}

int main(void){
    int x = 0, n = 0, even_odd = 0;
    printf("Enter x and n: ");
    scanf("%d %d", &x, &n);

    printf("%d^%d : %d\n", x, n, (n % 2 != 0) ? (power_of_n(x,n-1)*x) : (power_of_n(x,n)));
    return 0;
}
