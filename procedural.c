#include <stdio.h>

int x = 22; // global

void cambiaProcedimiento(int * pint){
    *pint += 1;
};

int f(int a){
    return a + 1;
}

void main(void) {

    printf("x; %d\n", x); // 22
    cambiaProcedimiento(&x);
    printf("x; %d\n", x); // 23
    x = f(x);
    printf("x; %d\n", x); // 24

}