#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,n,p,s=0,i;
    scanf("%d%d%d%d",&x,&y,&n,&p);
    for (i=0;i<n;i++)
        if ((1<<i)&y)
            s=s+(1<<i);
    for (i=0;i<p;i++)
        s=s<<1;
    for (i=p;i<=p+n;i++)
        p=p|s;
        printf("%d",p);

    return 0;
}
