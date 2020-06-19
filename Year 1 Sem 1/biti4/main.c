#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    unsigned long long x;
    int n=0,y[10],i,nr=0,k=0;
    scanf("%llu",&x);
    while (x)
    {
        n++;
        y[n]=x%10000;
        x=x/10000;
    }
    for (i=n; i>=1; i--)
    {
        nr=-1;
        k=0;
        if (y[i]<1010)
        {
            while (y[i])
            {
                nr++;
                if (y[i]%10==1)
                    k=k+pow(2,nr);
                y[i]=y[i]/10;
            }
            printf("%d",k);
        }
        if (y[i]==1010)
            printf("A");
        else if (y[i]==1011)
            printf("B");
        else if (y[i]==1100)
            printf("C");
        else if (y[i]==1101)
            printf("D");
        else if (y[i]==1110)
            printf("E");
        else if (y[i]==1111)
            printf("F");
    }

    return 0;
}
