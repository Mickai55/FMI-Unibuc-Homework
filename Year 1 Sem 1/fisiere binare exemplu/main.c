#include <stdio.h>
#include <stdlib.h>

void creare_fisier (char *nume_fisier, int n){
    FILE *out=fopen(nume_fisier,"wb");
    int i;
    for (i=0;i<n;i++)
    {
        int x=rand()%n;
        if (rand()%2==0)
            x=-x;
        fprintf(out,"%d ",x);
    }
    fclose(out);
}

int main()
{
    int n;
    scanf("%d",&n);
    creare_fisier("binar.bin",n);


    return 0;
}
