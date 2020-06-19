#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int id;
    char nume[20],prenume[20];
    int nota;
}student;

student s[3];

void creare (char *nume_fisier_binar, int n){
    FILE *fis1=fopen(nume_fisier_binar,"wb");
    for (int i=0;i<n;i++){
        fwrite(&s[i].id,sizeof(int),1,fis1);
        fwrite(&s[i].nume,sizeof(s[i].nume),1,fis1);///&&&
        fwrite(&s[i].prenume,sizeof(s[i].prenume),1,fis1);
        fwrite(&s[i].nota,sizeof(float),1,fis1);
    }
    fclose(fis1);
}

void afisare (char *nume_fisier_binar, char *nume_fisier_text, int n){
    FILE *fis1,*fis2;
    fis1=fopen(nume_fisier_binar,"rb");
    fis2=fopen(nume_fisier_text,"wt");
    for (int i=0;i<n;i++)
    {
        fread(&s[i].id,sizeof(int),1,fis1);
        fprintf(fis2,"%d ",s[i].id);
        fread(&s[i].nume,sizeof(s[i].nume),1,fis1);
        fprintf(fis2,"%s ",s[i].nume);
        fread(&s[i].prenume,sizeof(s[i].prenume),1,fis1);
        fprintf(fis2,"%s ",s[i].prenume);
        fread(&s[i].nota,sizeof(int),1,fis1);
        fprintf(fis2,"%d\n",s[i].nota);
    }
}

void modificare (char *nume_fisier_binar, int id, int nota){
    FILE *fis1=fopen(nume_fisier_binar,"rb+");
    int x;
    fseek(fis1,id*(2*sizeof(int)+40*sizeof(char)),SEEK_CUR);
    fseek(fis1,id*(sizeof(int)+40*sizeof(char)),SEEK_CUR);
    fwrite(&nota,sizeof(int),1,fis1);
}

int main()
{
    int n;
    scanf("%d",&n);
    int i;
    for (i=0;i<n;i++)
        scanf("%d %s %s %d",&s[i].id,&s[i].nume,&s[i].prenume,&s[i].nota);
    creare ("fisier",n);
    modificare("fisier",2,4);

    for (int i=0;i<n;i++)
        printf("%d %s %s %d \n",s[i].id,s[i].nume,s[i].prenume,s[i].nota);

    return 0;
}
/*
3
1 Pulica Popescu 7
2 Ionut Caca 4
3 Coiza Andrei 5
*/
