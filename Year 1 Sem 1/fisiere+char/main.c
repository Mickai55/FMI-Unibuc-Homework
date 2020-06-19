#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fisier1;
    char s[100];
    gets(s);
    fisier1=fopen("caca.txt","wt");
    fprintf(fisier1,"%s",s);


    return 0;
}
