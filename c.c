#include <stdio.h>
#include <sys/time.h>

#define MICROSECONDS 1000000

int f(int n) {
    if(n > 1) {
        return f(n - 1) + f(n - 2);
    }
    return 1;
}


int main(int argc, char** argv) {
    struct timeval start, end;
    gettimeofday(&start, 0);
    int result = f(40);
    gettimeofday(&end, 0);
    printf("%d\n", result);
    long mics = end.tv_sec * MICROSECONDS + end.tv_usec -
        (start.tv_sec * MICROSECONDS + start.tv_usec);
    printf("%d\n", mics/1000);
    return 0;
}
