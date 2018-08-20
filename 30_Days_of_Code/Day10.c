#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();



int main()
{

    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);
    int cnt=0, max_cnt=0, flag=0;

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }
    
    while(n){
        if(n%2 == 0){
            flag = 0;
            cnt = 0;
        }else{
            flag = 1;
            cnt++;
            if(max_cnt < cnt)
                max_cnt = cnt;
        }
        n /= 2;
    }
    printf("%d\n", max_cnt);
    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
