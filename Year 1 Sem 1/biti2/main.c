#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,x;
    scanf("%d%d",&x,&n);
    if ((1<<n)&x)
        printf("1");
    else
        printf("0");

    printf("\n************************\n");

    if ((1<<n)&x)
        printf("%d",x-(1<<n));
    else
        printf("%d",x);

    printf("\n************************\n");

    if (((1<<n)&x)==0)
        printf("%d",x+(1<<n));
    else
        printf("%d",x);


    return 0;
}
