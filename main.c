#include <stdio.h>

int f(int n) {
    if(n > 1) {
        return f(n - 1) + f(n - 2);
    }
    return 1;
}

int main(int argc, char** argv) {
    printf("%d\n", f(40));
    return 0;
}
