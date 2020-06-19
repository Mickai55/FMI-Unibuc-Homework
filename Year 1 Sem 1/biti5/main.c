#include <stdio.h>
#include <stdlib.h>

int main()
{
    int aux,s,x,y,k[100],i,n=0;
    scanf("%d",&x);
    while (1){
        scanf("%d",&y);
        if (y==0)
            break;
        aux=x;s=0;
        while (aux){
            s=s+aux%10;
            aux=aux/10;
        }
        if (y==x%s){
            n++;
            k[n]=x;
            n++;
            k[n]=y;
        }
        x=y;
    }
    for (i=1;i<=n;i=i+2){
        printf("%d %d",k[i],k[i+1]);
        printf("\n");
    }


    return 0;
}
