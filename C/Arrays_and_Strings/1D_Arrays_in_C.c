#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n, sum, val, i;
    
    sum = 0;
    scanf("%d", &n);
    //printf("%d", n);
    for(i=0; i<n; i++){
        scanf("%d", &val);
        sum += val;
    }
    printf("%d\n", sum);
    return 0;
}
