#include <stdio.h>
#include <math.h>

/*
Ref: [求質數演算法的N種境界](https://www.getit01.com/p201807213917086/)
gcc Day25.c -lm
*/

int is_prime(int data)
{
	int i, squart_root;

    if (data == 2)
        return 1;
    else if ((data == 1) || (data % 2 == 0))
        return 0;
    
    squart_root = (int)sqrt(data);
    for(i=3; i <= squart_root; i++){
        if(data % i == 0)
            return 0;
	}

    return 1;
}

int main()
{
    int T, data;
    scanf("%d",&T);
    while(T-- > 0){
        scanf("%d",&data);
        if(is_prime(data))
            printf("Prime\n");
        else
            printf("Not prime\n");
    }

    return 0;
}
