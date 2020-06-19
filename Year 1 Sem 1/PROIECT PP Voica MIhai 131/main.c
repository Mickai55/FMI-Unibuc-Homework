#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
    unsigned char r, g, b;
} pixel;

typedef struct
{
    double val;
    int i, j, cif, sters;
} fereastra;

void liniarizare (char* nume_fisier_sursa, pixel **p, int *k, int *latime, int *inaltime, unsigned char **header)
{
    FILE *fin;

    fin = fopen(nume_fisier_sursa, "rb");
    if(fin == NULL)
    {
        printf("Nu a fost gasita imaginea sursa.");
        return;
    }

    fseek(fin, 18, SEEK_SET);
    fread(&(*latime), sizeof(unsigned int), 1, fin);
    fread(&(*inaltime), sizeof(unsigned int), 1, fin);

    *latime = *latime + (4 - (*latime % 4)) % 4;

    *header = (unsigned char*) malloc (54 * sizeof(unsigned char));
    fseek(fin, 0, SEEK_SET);
    fread ((*header), 54, 1, fin);

    *p = (pixel*) malloc (*latime * *inaltime * (sizeof(pixel)));

    fseek(fin, 54, SEEK_SET);
    for(int i = 0; i < *inaltime; i++)
        for(int j = 0; j < *latime; j++)
        {
            fread(&(*p)[i * *latime + j].b, sizeof(unsigned char), 1, fin);
            fread(&(*p)[i * *latime + j].g, sizeof(unsigned char), 1, fin);
            fread(&(*p)[i * *latime + j].r, sizeof(unsigned char), 1, fin);
            (*k)++;
        }
    fclose(fin);
}

void xorshift32 (unsigned int **r, int k, unsigned int cheie1)
{
    *r = (unsigned int*) malloc (2 * k * sizeof (unsigned int));
    (*r)[0] = cheie1;
    unsigned int x = cheie1;
    for (int i = 1; i < 2 * k; i++)
    {
        x = x ^ x << 13;
        x = x ^ x >> 17;
        x = x ^ x << 5;
        (*r)[i] = x;
    }
}

void Durstenfeld (unsigned int **x, unsigned int *r, int k)
{
    *x = (unsigned int*) malloc ( k * sizeof (unsigned int));
    unsigned int i, j, aux;
    for (i = 0; i < k; i++)
        (*x)[i] = i;
    for (i = k - 1; i >= 1; i--)
    {
        j = r[k - i] % (i + 1);
        aux = (*x)[j];
        (*x)[j] = (*x)[i];
        (*x)[i] = aux;
    }
}

void Xsquared (pixel *p, int k)
{
    unsigned int *f_r, *f_g, *f_b;
    f_r = (unsigned int*) calloc (k, sizeof (unsigned int));
    f_g = (unsigned int*) calloc (k, sizeof (unsigned int));
    f_b = (unsigned int*) calloc (k, sizeof (unsigned int));
    int i;
    for (i = 0; i < k; i++)
    {
        f_r[p[i].r]++;
        f_g[p[i].g]++;
        f_b[p[i].b]++;
    }
    double F = k / 256, F_r = 0, F_g = 0,F_b = 0;
    for (i = 0; i <= 255; i++)
    {
        F_r += ((f_r[i] - F) * (f_r[i] - F)) / F;
        F_g += ((f_g[i] - F) * (f_g[i] - F)) / F;
        F_b += ((f_b[i] - F) * (f_b[i] - F)) / F;
    }
    printf("R: %0.2f\nG: %0.2f\nB: %0.2f\n\n", F_r, F_g, F_b);

    free(f_r);
    free(f_g);
    free(f_b);
}

void xors (pixel *P, int k, unsigned int *r, pixel **c, int cheie2)
{
    unsigned int SV = cheie2;
    unsigned char x2 = 0, x1 = 0, x0 = 0, q = 0;

    *c = (pixel*) malloc (k * (sizeof(pixel)));

    x0 = x0 | SV;
    x1 = x1 | (SV >> 8);
    x2 = x2 | (SV >> 16);

    q = r[k] >> 16;
    (*c)[0].r = P[0].r ^ x2 ^ q;

    q = r[k] >> 8;
    (*c)[0].g = P[0].g ^ x1 ^ q;

    q = r[k];
    (*c)[0].b = P[0].b ^ x0 ^ q;

    for (int i = 1; i < k; i++)
    {
        q = r[k + i] >> 16;
        (*c)[i].r = (*c)[i - 1].r ^ P[i].r ^ q;

        q = r[k + i] >> 8;
        (*c)[i].g = (*c)[i - 1].g ^ P[i].g ^ q;

        q = r[k + i];
        (*c)[i].b = (*c)[i - 1].b ^ P[i].b ^ q;
    }
}

void creare_imagine (pixel *p, int latime, int inaltime, char *imagine_noua, unsigned char *header)
{
    FILE *fout;
    fout = fopen(imagine_noua, "wb+");
    if (fout == NULL)
        printf("Nu s-a deschis.");

    fwrite (header, 54, 1, fout);
    fseek(fout, 54, SEEK_SET);

    for(int i = 0; i < inaltime; i++)
        for(int j = 0; j < latime; j++)
        {
            fwrite(&p[i * latime + j].b, sizeof(unsigned char), 1, fout);
            fwrite(&p[i * latime + j].g, sizeof(unsigned char), 1, fout);
            fwrite(&p[i * latime + j].r, sizeof(unsigned char), 1, fout);
        }
    fclose (fout);
}

void CRIPTARE (char *nume_imagine_initiala, char *nume_imagine_criptata, char *cheie_secreta)
{
    pixel *p, *P, *c;
    int k=0, i, cheie1, cheie2, latime, inaltime;
    unsigned int *r, *x;
    unsigned char *header;

    ///citire chei secrete

    FILE *fis = fopen (cheie_secreta, "rt");
    fscanf (fis, "%d%d", &cheie1, &cheie2);

    ///liniarizare imagine

    liniarizare(nume_imagine_initiala, &p, &k, &latime, &inaltime, &header);

    ///generare numere random

    xorshift32(&r, k, cheie1);

    ///permutare pixeli

    P = (pixel*) malloc (k * (sizeof(pixel)));
    Durstenfeld(&x, r, k);
    for (i = 0; i < k; i++)
        P[x[i]] = p[i];

    ///xor-are pixeli

    xors(P, k, r, &c, cheie2);

    ///test XSquared

    Xsquared(p, k);

    ///creare imagine criptata

    creare_imagine(c, latime, inaltime, nume_imagine_criptata, header);

    fclose(fis);
    free(p);
    free(P);
    free(c);
    free(x);
    free(r);
    free(header);
}

void xors_inv (pixel *P, int k, unsigned int *r, pixel **C, int cheie2)
{
    unsigned int SV = cheie2;
    unsigned char x2 = 0, x1 = 0, x0 = 0, q = 0;
    *C = (pixel*) malloc (k * (sizeof(pixel)));
    x0 = x0 | SV;
    x1 = x1 | (SV >> 8);
    x2 = x2 | (SV >> 16);

    q = r[k] >> 16;
    (*C)[0].r = P[0].r ^ x2 ^ q;

    q = r[k] >> 8;
    (*C)[0].g = P[0].g ^ x1 ^ q;

    q = r[k];
    (*C)[0].b = P[0].b ^ x0 ^ q;

    for (int i = 1; i < k; i++)
    {
        q = r[k+i] >> 16;
        (*C)[i].r = P[i-1].r ^ P[i].r ^ q;

        q = r[k+i] >> 8;
        (*C)[i].g = P[i-1].g ^ P[i].g ^ q;

        q = r[k+i];
        (*C)[i].b = P[i-1].b ^ P[i].b ^ q;
    }
}

void DECRIPTARE (char *nume_imagine_criptata, char *nume_imagine_decriptata, char *cheie_secreta)
{
    pixel *c, *C, *D;
    int k=0, i, cheie1, cheie2, latime, inaltime;
    unsigned int *r, *x;
    unsigned char *header;

    ///citire chei secrete

    FILE *fis = fopen (cheie_secreta,"rt");
    fscanf (fis, "%d%d", &cheie1, &cheie2);

    ///liniarizare imagine criptata

    liniarizare(nume_imagine_criptata, &c, &k, &latime, &inaltime, &header);///p=C

    ///generare numere random

    xorshift32(&r, k, cheie1);

    ///xor-are inversa pixeli

    xors_inv(c, k, r, &C, cheie2);

    ///permutare inversa pixeli

    D = (pixel*) malloc (k * (sizeof(pixel)));
    Durstenfeld(&x, r, k);
    for (i = 0; i < k; i++)
        D[i] = C[x[i]];

    ///test XSquared

    Xsquared(c, k);

    ///creare imagine decriptata

    creare_imagine(D, latime, inaltime, nume_imagine_decriptata, header);

    fclose(fis);
    free(c);
    free(D);
    free(C);
    free(r);
    free(x);
    free(header);
}

int compare (const void * a, const void * b)
{
    if (*(double*)a > *(double*)b)
        return -1;
    else if (*(double*)a < *(double*)b)
        return 1;
    return 0;
}

void liniarizare_cifra (char* nume_fisier_sursa, pixel **p)
{
    FILE *fin;
    int latime, inaltime;
    fin = fopen(nume_fisier_sursa, "rb");

    if(fin == NULL)
    {
        printf("Nu a fost gasita imaginea sursa.");
        return;
    }

    fseek(fin, 18, SEEK_SET);
    fread(&latime, sizeof(unsigned int), 1, fin);
    fread(&inaltime, sizeof(unsigned int), 1, fin);

    latime = latime + (4 - (latime % 4)) % 4;

    *p = (pixel*) malloc (latime * inaltime * (sizeof(pixel)));

    fseek(fin, 54, SEEK_SET);
    for(int i = 0; i < inaltime; i++)
        for(int j = 0; j < latime; j++)
        {
            fread(&(*p)[i * latime + j].b, sizeof(unsigned char), 1, fin);
            fread(&(*p)[i * latime + j].g, sizeof(unsigned char), 1, fin);
            fread(&(*p)[i * latime + j].r, sizeof(unsigned char), 1, fin);
        }

    fclose(fin);
}

void grayscale (pixel *tabla, int k)
{
    unsigned char aux;
    for(int i = 0; i < k; i++)
    {
            aux = tabla[i].r * 0.299 + tabla[i].g * 0.587 + tabla[i].b * 0.114;
            tabla[i].r = aux;
            tabla[i].g = aux;
            tabla[i].b = aux;
    }
}

double intensitateGS (pixel *p, int k, int i1, int i2, int j1, int j2, int latime)
{
    double s = 0;
    for (int i = i1; i < i2; i++)
        for (int j = j1; j < j2; j++)
            s = s + p[i * latime + j].r;

    return s / k;
}

double deviatie_standard (pixel *p, int k, int i1, int i2, int j1, int j2, double q, int latime)
{
    double s = 0;
    for (int i = i2 - 1; i >= i1; i--)
        for (int j = j1; j < j2; j++)
            s = s + (p[i * latime + j].r - q) * (p[i * latime + j].r - q);

    return sqrt(s / (k - 1));
}

double corr (pixel *cif, int k, pixel *fer,  int i1, int i2, int j1, int j2, int latime)
{
    int u = 0;
    double s = 0;
    double intens_gs_cif = intensitateGS(cif, k, 0, 15, 0 ,12, 12);
    double dev_st_cif = deviatie_standard(cif, k, 0, 15, 0, 12, intens_gs_cif, 12);
    double intens_gs_fer = intensitateGS(fer, k, i1, i2, j1, j2, latime);
    double dev_st_fer = deviatie_standard(fer, k, i1, i2, j1, j2, intens_gs_fer, latime);

    for (int i = i1; i < i2; i++)
        for (int j = j1; j < j2; j++)
        {
            u++;
            s = s + (((fer[i * latime + j].r - intens_gs_fer) * (cif[u].r - intens_gs_cif)) / (dev_st_cif * dev_st_fer));
        }

    return s / k;
}

void colorare_margini (pixel *tabla, int i1, int i2, int j1, int j2, int latime, int R, int G, int B)
{
    for (int i = i1; i < i2; i++)
        for (int j = j1; j < j2; j++)
            if (i == i1 || j == j1 || i == i2 - 1 || j == j2 - 1)
            {
                    tabla[i * latime + j].r = R;
                    tabla[i * latime + j].g = G;
                    tabla[i * latime + j].b = B;
            }
}

void corelatii (pixel *cif, int k, pixel *test, int latime, int inaltime, fereastra **D, int *p, int cifra_curenta)
{
    double q;
    for (int i = 0; i < inaltime - 15; i++)
        for (int j = 0; j < latime - 12; j++)
        {
            q = corr (cif, k, test, i, i + 15, j, j + 12, latime);
            if (q > 0.5)
            {
                (*D)[*p].val = q;
                (*D)[*p].i = i;
                (*D)[*p].j = j;
                (*D)[*p].cif = cifra_curenta;
                (*D)[*p].sters = 0;
                (*p)++;
            }
        }
}

int aria_intesectie (int i1, int j1, int I1, int J1)
{
    int i, j;
    i = abs(I1 - i1);
    j = abs(J1 - j1);
    if (i > 16 || j > 12)
        return 0;

    return (15 - i) * (12 - j);
}

double suprapunere (int i1, int j1, int I1, int J1)
{
    int aria_int = aria_intesectie(i1, j1, I1, J1);
    return (double) aria_int / (360 - aria_int);
}

void eliminare_non_maxime (fereastra **D, int p)
{
    for (int i = 0; i < p - 1; i++)
        for (int j = i + 1; j < p; j++)
            if ((*D)[j].sters == 0 && suprapunere((*D)[i].i, (*D)[i].j, (*D)[j].i, (*D)[j].j) > 0.2)
                (*D)[j].sters = 1;
}

void template_matching(char *tablou, char *c0, char *c1, char *c2, char *c3, char *c4, char *c5, char *c6, char *c7, char *c8, char *c9)
{
    pixel *tabla, *cifra, *test ;
    int latimeTabla, inaltimeTabla, kTabla = 0, latimeT, inaltimeT, k = 0, kc = 180,  p = 0;
    unsigned char *headerT, *headerTabla;
    fereastra *D;

    ///liniarizare imagine principala

    liniarizare(tablou, &tabla, &kTabla, &latimeTabla, &inaltimeTabla, &headerTabla);

    ///creare imagine grayscale

    liniarizare(tablou, &test, &k, &latimeT, &inaltimeT, &headerT);
    grayscale(test, k);

    ///creare tablou de detectii cu fiecare cifra

    D = (fereastra*) malloc (10 * latimeT * inaltimeT * sizeof(fereastra));

    liniarizare_cifra(c0, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 0);

    liniarizare_cifra(c1, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 1);

    liniarizare_cifra(c2, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 2);

    liniarizare_cifra(c3, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 3);

    liniarizare_cifra(c4, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 4);

    liniarizare_cifra(c5, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 5);

    liniarizare_cifra(c6, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 6);

    liniarizare_cifra(c7, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 7);

    liniarizare_cifra(c8, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 8);

    liniarizare_cifra(c9, &cifra);
    grayscale(cifra, kc);
    corelatii(cifra, kc, test, latimeT, inaltimeT, &D, &p, 9);

    ///sortare tablou de detectii

    qsort(D, p, sizeof(fereastra), compare);

    ///eliminare non-maxime

    eliminare_non_maxime(&D, p);

    ///colorare margini la detectiile ramase

    for (int i = 0; i < p; i++)
        if (D[i].sters == 0)
        {
            if (D[i].cif == 0)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 255, 0, 0);
            if (D[i].cif == 1)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 255, 255, 0);
            if (D[i].cif == 2)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 0, 255, 0);
            if (D[i].cif == 3)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 0, 255, 255);
            if (D[i].cif == 4)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 255, 0, 255);
            if (D[i].cif == 5)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 0, 0, 255);
            if (D[i].cif == 6)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 192, 192, 192);
            if (D[i].cif == 7)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 255, 140, 0);
            if (D[i].cif == 8)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 128, 0, 128);
            if (D[i].cif == 9)
                colorare_margini(tabla,D[i].i, D[i].i+15, D[i].j, D[i].j+12, latimeT, 128, 0, 0);
        }

    ///creare imagine cu cifrele recunoscute

    creare_imagine(tabla, latimeT, inaltimeT, "Gasire_cifre.bmp", headerT);

    free(D);
    free(headerT);
    free(tabla);
    free(cifra);
    free(test);
    free(headerTabla);

}

int main()
{
    printf("-CRIPTARE/DECRIPTARE-\n\n");

    FILE *fisier_intrare_criptare;
    char imagine_sursa[50],  imagine_criptata[20], imagine_decriptata[20], cheie_secreta[20];
    fisier_intrare_criptare = fopen("fisier_intrare_criptare.txt", "rt");

    if (fisier_intrare_criptare == NULL)
    {
        printf("Nu s-a deschis fisierul de intrare 1");
        return;
    }

    fscanf (fisier_intrare_criptare, "%s", &imagine_sursa);
    fscanf (fisier_intrare_criptare, "%s", &imagine_criptata);
    fscanf (fisier_intrare_criptare, "%s", &cheie_secreta);
    fscanf (fisier_intrare_criptare, "%s", &imagine_decriptata);

    printf("Valorile Xsquared ale imaginii '%s' inainte de criptare:\n", imagine_sursa);

    CRIPTARE (imagine_sursa, imagine_criptata, cheie_secreta);

    printf("Valorile Xsquared ale imaginii criptate: '%s':\n", imagine_criptata);

    DECRIPTARE (imagine_criptata, imagine_decriptata, cheie_secreta);

    fclose(fisier_intrare_criptare);

    printf("-CRIPTARE/DECRIPTARE REALIZATA CU SUCCES-\n\n");

    printf("-TEMPLATE MATCHING-\n\n");

    FILE *fisier_intrare_template;
    char tablou[50], c0[20], c1[20], c2[20], c3[20], c4[20], c5[20], c6[20], c7[20], c8[20], c9[20];
    fisier_intrare_template = fopen("fisier_intrare_template.txt", "rt");

    if (fisier_intrare_template == NULL)
    {
        printf("Nu s-a deschis fisierul de intrare 2");
        return;
    }

    fscanf (fisier_intrare_template, "%s", &tablou);
    fscanf (fisier_intrare_template, "%s", &c0);
    fscanf (fisier_intrare_template, "%s", &c1);
    fscanf (fisier_intrare_template, "%s", &c2);
    fscanf (fisier_intrare_template, "%s", &c3);
    fscanf (fisier_intrare_template, "%s", &c4);
    fscanf (fisier_intrare_template, "%s", &c5);
    fscanf (fisier_intrare_template, "%s", &c6);
    fscanf (fisier_intrare_template, "%s", &c7);
    fscanf (fisier_intrare_template, "%s", &c8);
    fscanf (fisier_intrare_template, "%s", &c9);

    template_matching(tablou, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9);

    fclose(fisier_intrare_template);

    printf("-TEMPLATE MATCHING REALIZAT CU SUCCES-\n");

    return 0;
}

