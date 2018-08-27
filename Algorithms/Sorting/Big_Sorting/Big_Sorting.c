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

// Complete the bigSorting function below.

// Please store the size of the string array to be returned in result_count pointer. For example,
// char a[2][6] = {"hello", "world"};
//
// *result_count = 2;
//
// return a;
//
void swap(char** unsorted, int i, int j)
{
    char *tmp;
    
    tmp = *(unsorted+i);
    *(unsorted+i) = *(unsorted+j); 
    *(unsorted+j) = tmp;
}

int is_bigger(char** unsorted, int i, int j){
    int rlt;
    
    if(strlen(*(unsorted+i)) > strlen(*(unsorted+j)))
        rlt = 1;
    else if (strlen(*(unsorted+i)) < strlen(*(unsorted+j)))
        rlt = -1;
    else
        rlt = strcmp(*(unsorted+i), *(unsorted+j));
    //printf("comapre: %s, %s, %d\n", *(unsorted+i), *(unsorted+j), rlt);
    return rlt;
}

void quick_sort_recursive(char** unsorted, int start, int end) 
{
    int i;                    // counter
    int pivot_idx = end;      // pivot element index
    int sorted_idx = start;   // divide position for pivot element
    
    if(start >= end)
        return;
    //printf("%s() %d, %d\n", __func__, start, end);
    for(i = start; i<end; i++){
        if((is_bigger(unsorted, i, pivot_idx) < 0)){
            swap(unsorted, i, sorted_idx);
            sorted_idx++;
        }        
    }
    swap(unsorted, pivot_idx, sorted_idx);
    quick_sort_recursive(unsorted, start, sorted_idx-1);
    quick_sort_recursive(unsorted, sorted_idx+1, end);  
}


char** bigSorting(int unsorted_count, char** unsorted, int* result_count) {
    int i;
    *result_count = unsorted_count;
    quick_sort_recursive(unsorted, 0, unsorted_count-1);
    return unsorted;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    char** unsorted = malloc(n * sizeof(char*));

    for (int i = 0; i < n; i++) {
        char* unsorted_item = readline();

        *(unsorted + i) = unsorted_item;
    }
    #if 0
    printf("comapre: %s, %s, %d\n", *(unsorted), *(unsorted+1), strcmp(*(unsorted), *(unsorted+1)));
    printf("comapre: %s, %s, %d\n", *(unsorted+1), *(unsorted), strcmp(*(unsorted+1), *(unsorted)));
    printf("comapre: %s, %s, %d\n", *(unsorted+1), *(unsorted+1), strcmp(*(unsorted+1), *(unsorted+1)));
    printf("comapre: %s, %s, %d\n", *(unsorted+1), *(unsorted+2), strcmp(*(unsorted+1), *(unsorted+2)));
    printf("comapre: %s, %s, %d\n", *(unsorted+2), *(unsorted+1), strcmp(*(unsorted+2), *(unsorted+1)));
    printf("comapre: %s, %s, %d\n", *(unsorted), *(unsorted+5), strcmp(*(unsorted), *(unsorted+5)));
    #endif

    int unsorted_count = n;

    int result_count;
    char** result = bigSorting(unsorted_count, unsorted, &result_count);

    
    for (int i = 0; i < result_count; i++) {
        fprintf(fptr, "%s", *(result + i));

        if (i != result_count - 1) {
            fprintf(fptr, "\n");
        }
    }

    fprintf(fptr, "\n");

    fclose(fptr);

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
