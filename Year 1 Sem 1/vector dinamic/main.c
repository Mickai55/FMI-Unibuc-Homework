#include <stdio.h>
#include <stdlib.h>

void functie (int *v, int n, int **x, int *k)
{
    *x = (int*) malloc (n * sizeof(int));
    for (int i = 0; i < n; i++)
        if (v[i] % 2 == 0)
        {
            (*x)[*k] = v[i];
            (*k)++;
        }
}

int main()
{
    int v[100] = {1, 2, 3, 4, 5, 6}, *x, k = 0, n = 6;
    functie (v, n, &x, &k);
    for (int i = 0; i < k; i++)
        printf("%d ", x[i]);


    return 0;
}
