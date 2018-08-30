#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n, tmp; 
    int numSwaps = 0;
    
    scanf("%d", &n);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
    	scanf("%d",&a[a_i]);
    }
    // Write Your Code Here
    
    for (int i = 0; i < n; i++) {
    int numberOfSwaps = 0;
    
        for (int j = 0; j < n - 1; j++) {
            if (a[j] > a[j + 1]) {
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                numberOfSwaps++;
            }
        }
        numSwaps += numberOfSwaps;

        if (numberOfSwaps == 0) {
            break;
        }
    }
    printf("Array is sorted in %d swaps.\n", numSwaps);
    printf("First Element: %d\n", a[0]);
    printf("Last Element: %d\n", a[n-1]);
    return 0;
}
