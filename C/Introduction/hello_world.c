#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


/* 
	Ref:
		Scanf的困惑(https://blog.csdn.net/mickey35/article/details/52624534)
		format ‘%s’ expects argument of type ‘char *’, but argument 2 has type ‘char (*)[64](https://stackoverflow.com/questions/19439525/format-s-expects-argument-of-type-char-but-argument-2-has-type-char/19439537)
*/
int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", s);
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    printf("Hello, World!\n%s\n", s);
    return 0;
}
