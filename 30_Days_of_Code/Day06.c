#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
    int i, j;
    char* p_strs[10];             // 1 <= T <= 10
    char pre[5000], pos[5000];    // 2 <= length of S <= 10000
    int pre_i, pos_i;

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    for(i=0; i<n; i++){
        p_strs[i] = readline();
    }

    for(i=0; i<n; i++){
        pre_i = pos_i = 0;
        for(j=0; j<strlen(p_strs[i]); j++){
            if(j%2 == 0){
                pre[pre_i++] = p_strs[i][j];
            }else{
                pos[pos_i++] = p_strs[i][j];
            }
        }
        pre[pre_i] = pos[pos_i]= '\0';
        printf("%s %s\n", pre, pos);
    }

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
