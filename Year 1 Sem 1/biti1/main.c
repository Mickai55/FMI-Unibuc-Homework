#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,i,k=0,sw=0;
    scanf("%d",&a);
    for (i=31;i>=0;i--)
        if (a&(1<<i)){
            sw=1;
            printf("1");
        }
        else
            if (sw==1)
                printf("0");



    return 0;
}
