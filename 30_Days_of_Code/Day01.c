#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";


    // Declare second integer, double, and String variables.
    int v_i;
    double v_d;
    char v_s[128];

    // Read and save an integer, double, and String to your variables.
    scanf("%d", &v_i);
    scanf("%lf", &v_d);
    scanf(" %[^\n]", v_s);

    // Print the sum of both integer variables on a new line.
    printf("%d\n", v_i + i);

    // Print the sum of the double variables on a new line.
    printf("%.1lf\n", v_d + d);

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    printf("%s%s\n", s, v_s);
    //printf("%s\n", s);
    //printf("%s\n", v_s);
}
