#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    /*
    char str[1000];
    int cnt[10], i;
    
    scanf("%s", str);
    // printf("%s, len=%d\n", str, strlen(str));
    memset(cnt, 0, sizeof(cnt));
    for(i=0; i<strlen(str); i++){
        if(str[i] >= '0' && str[i] <= '9'){
            cnt[str[i] - '0']++;
        }
    }
        
    for(i=0; i<10; i++)
        printf("%d ", cnt[i]);
    */
    int cnt[10], i;
    char c;
    
    /* scanf()
        Return Value
        If successful, the total number of characters written is returned, 
        otherwise a negative number is returned.
    */
    memset(cnt, 0, sizeof(cnt));
    while(scanf("%c", &c) == 1){
        printf("%d\n", scanf("%c", &c) );
        printf("%c", c);
        if(c >= '0' && c <= '9')
            cnt[c - '0']++;
    }
    scanf("%c", &c);
    for(i=0; i<10; i++)
        printf("%d ", cnt[i]);
    return 0;
}
