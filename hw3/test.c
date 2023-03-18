#include <stdlib.h>
#include <stdio.h>
void function(int a, int b, int c) {
    char buffer1[5];
    char buffer2[20];
    int *ret;
    // buffer2[0] = 1;
    // buffer1[0] = 2;
    ret = buffer1 + 12;
    (*ret) += 7;
}

void main() {
    int x;
    x = 0;
    function(1,2,3);
    x = 1;
    printf("x=%d\n", x);
}
