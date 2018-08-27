* Big Sorting
  * Ref: [quicksort-in-place.c](https://github.com/strncat/competitive-programming/blob/master/hacker-rank/algorithms/sorting/quicksort-in-place.c)
  * There is a problem in C. I can convert string to integer if the number is too big. So I comapre the two strings of number with
    * a > b if strlen(a) > strlen(b)
    * a < b if strlen(a) < strlen(b)
    * strcmp(a, b) if strlen(a) == strlen(b)
