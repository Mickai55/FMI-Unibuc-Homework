#include <stdio.h>
#include <stdlib.h>

int main()
{
   /* FILE *fis;
    char *sir;
    sir = malloc (50*sizeof(char));
    fis=fopen("exemplu.txt","rt");
    fgets(sir,50,fis);
    printf("%s",sir);
    free(sir);
*/
    FILE *fis;
    char sir[50];
    fis=fopen("exemplu.txt","rt");
    fgets(sir,50,fis);
    printf("%s",sir);
    free(sir);

    return 0;
}
