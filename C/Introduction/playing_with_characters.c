#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    // Ref: [scanf](http://www.cplusplus.com/reference/cstdio/scanf/)    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    #define MAX_LEN 128
    char ch;
    char s[MAX_LEN];
    char sen[MAX_LEN];

    # if 1
    scanf("%c", &ch);
    // Read from stream, escape the new line from previous line. 
    scanf("%s", s);     
    // The space in the beginning of the format string tells it to ignore the newline character 
    // from the previous line (newlines are considered whitespace here)    
    // %[^\n]: scans everything until a \n (not \n)
    // %*c: the data(specifier is character) is to be read from the stream but ignored
    scanf(" %[^\n]%*c", sen);
    #else
    // Add the ignore character statement to the first two lines, which will get rid of the 
    // newline characters from them allowing the read line statement to work correctly
    scanf("%c%*c", &ch);
    scanf("%s%*c", s);
    scanf("%[^\n]%*c", sen);
    #endif
    
    printf("%c\n%s\n%s\n", ch, s, sen);
    return 0;

}
