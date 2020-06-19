#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=65;
    FILE *fisier1,*fisier2;
    fisier2 = fopen("bin1.bin","wb");
    fwrite(&x,sizeof(int),1,fisier2);
    fclose(fisier2);

    return 0;
}
