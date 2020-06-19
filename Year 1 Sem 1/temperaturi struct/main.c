#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    char nume[20];
    float temp;
} oras;

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main()
{
    oras *O;
    O = (oras*) malloc(100*sizeof(oras));
    int k=0;
    float Max=0;
    FILE *fis1 = fopen("temperaturi.txt","rt");
    FILE *fis2 = fopen("maxime.txt","wt+");
    if (fis1==NULL||fis2==NULL)
        printf("Nu s-a deschis");
    while (!feof(fis1))
    {
        fscanf(fis1,"%s%f",&O[k].nume,&O[k].temp);
        k++;
    }
    /*
    for (int i=0; i<k; i++)
        printf("%s %f\n",O[i].nume,O[i].temp);
    for (int i=0; i<k; i++)
        if (O[i].temp>Max)
            Max=O[i].temp;
    fprintf(fis2,"%f \n",Max);
    for (int i=0; i<k; i++)
        if (O[i].temp==Max)
            fprintf(fis2,"%s\n", O[i].nume);
    */
    char u[20];float aux;
    for (int i=0; i<k-1; i++)
    for (int j=i; j<k; j++)
        if (O[i].temp==O[j].temp&&strcmp(O[i].nume,O[j].nume)>0){
            strcpy(u,O[i].nume);
            strcpy(O[i].nume,O[j].nume);
            strcpy(O[j].nume,u);
        }
        else if (O[i].temp>O[j].temp){
            aux=O[i].temp;
            O[i].temp=O[j].temp;
            O[j].temp=aux;
            strcpy(u,O[i].nume);
            strcpy(O[i].nume,O[j].nume);
            strcpy(O[j].nume,u);
    }
    for (int i=0; i<k; i++)
        printf("%s %f\n",O[i].nume,O[i].temp);


    return 0;
}
