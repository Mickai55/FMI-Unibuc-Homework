#include <stdio.h>
#include <stdlib.h>
#include <string.h>
FILE *fisier1,*fisier2;
void Recursie_Sjmechera()
{
    char s[100];
    if(!fgets(s,100,fisier1))
        return;
    Recursie_Sjmechera(s);
    printf("%s",s);
}

int main()
{
    fisier1=fopen("fis1.txt","rt");
    fisier2=fopen("fis2.txt","wt");

    Recursie_Sjmechera();

    fclose(fisier1);
    fclose(fisier2);




    return 0;
}
