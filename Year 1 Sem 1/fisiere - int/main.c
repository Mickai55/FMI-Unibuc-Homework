#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    FILE *fisier1,*fisier2;
    fisier1 = fopen ("date.in","rt");
    fisier2 = fopen ("date.out","wt");
    fscanf(fisier1,"%d",&x);
    fprintf(fisier2,"%d",2*x);
    fclose(fisier1);
    fclose(fisier2);

    return 0;
}
