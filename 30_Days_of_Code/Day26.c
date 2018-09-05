#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int act_day, act_mon, act_year;
    int exp_day, exp_mon, exp_year;

    scanf("%d %d %d", &act_day, &act_mon, &act_year);
    scanf("%d %d %d", &exp_day, &exp_mon, &exp_year);
    // printf("%d %d %d\n", act_day, act_mon, act_year);
    // printf("%d %d %d\n", exp_day, exp_mon, exp_year);
    
    if(act_year > exp_year){
        printf("10000\n");
        return 0;
    }else if (act_year == exp_year){
        if(act_mon > exp_mon){
            printf("%d\n", (act_mon - exp_mon) * 500);
            return 0;
        }else if(act_mon == exp_mon){
            if(act_day > exp_day){
                printf("%d\n", (act_day - exp_day) * 15);
                return 0;
            }
        }
    }
    printf("0\n");
    return 0;
}
