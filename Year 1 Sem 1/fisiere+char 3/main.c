#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *fisier1,*fisier2;
    int n=0,i;
    char s[100],k[100][100];
    fisier1=fopen("fis1.txt","rt");
    fisier2=fopen("fis2.txt","wt");
    while (fgets(s,100,fisier1))
    {
        strcpy(k[n],s);
        n++;
    }
    for (i=n;i>=0;i--)
        fprintf(fisier2,"%s",k[i]);

    fclose(fisier1);
    fclose(fisier2);

    return 0;
}
