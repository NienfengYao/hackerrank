#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function  
    int val1, val2;
    
    val1 = *a + *b;
    val2 = abs(*a - *b);
    *a = val1;
    *b = val2;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
