#include <stdio.h>
#include <stdlib.h>

void functie(int *k){
    *k=9;
}

int main()
{
    int k=3;
    functie (&k);
    printf("%d",k);


    return 0;
}
