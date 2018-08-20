/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

typedef struct books{
    char name[16];
    char phone[16];
} Books;
Books items[100000];

int main() {
    int n, i=0, found;
    Books new_item;

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    scanf("%d", &n);
    for(i=0; i<n; i++){
        memset(&new_item, 0, sizeof(new_item));
        scanf("%s", new_item.name);
        scanf("%s", new_item.phone);
        strcpy(items[i].name, new_item.name);
        strcpy(items[i].phone, new_item.phone);
    }

    //printf("sizeof: %d\n", (int)sizeof(new_item.name));
    fgets(new_item.name, sizeof(new_item.name), stdin); // Remove redundant input
    while(1){
        memset(new_item.name, 0, sizeof(new_item.name));
        fgets(new_item.name, sizeof(new_item.name), stdin);
        //printf("debug: %d \n", (int)strlen(new_item.name));
        //for(i=0; i<strlen(new_item.name); i++)
        //    printf("0x%x", new_item.name[i]);
        

        // The input behaveir is different between my pc and hackerrank server, so I check multiple condition
        if(strlen(new_item.name) == 0 || strcmp(new_item.name, "\n") == 0 )
            break;

        //printf("org: %d -%s-\n", (int)strlen(new_item.name), new_item.name);
        if(new_item.name[strlen(new_item.name)-1] == '\n'){
            new_item.name[strlen(new_item.name)-1] = '\0';  // replace '\n' with '\0'
        }
        //printf("%d %s\n", (int)strlen(new_item.name), new_item.name);

        found = 0;
        for(i=0; i<n; i++){
            //printf("%d, %s, %d, %s\n", (int)strlen(items[i].name), items[i].name, (int)strlen(new_item.name), new_item.name);
            if(strcmp(items[i].name, new_item.name) == 0){
                printf("%s=%s\n", items[i].name, items[i].phone);
                found = 1;
                break;
            }
        }
        if(!found)
            printf("Not found\n");
    }

    return 0;
}
