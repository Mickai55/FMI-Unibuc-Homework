#include <stdio.h>
#include <stdlib.h>

int main()
{
    int p,i,j,k;
    scanf("%d",&p);
    for (i=1;i<=p;i++)
        for (j=1;j<=p;j++){
            k=sqrt(i*i+j*j);
            if (i+j+k==p)
                printf("%d %d %d\n",i,j,k);
        }

    return 0;
}
