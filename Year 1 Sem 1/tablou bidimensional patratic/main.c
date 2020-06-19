#include <stdio.h>
#include <stdlib.h>

int** matrice (int n)
{
    int **x;
    x = (int **) calloc (n, sizeof(int*));
    for (int i = 0; i < n; i++)
        x[i] = (int*) calloc (i + 1, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        x[i][0] = i + 1;
        x[n - 1][i] = n - i;
    }
    for (int i = n - 2; i >= 0; i--)
        for (int j = 1; j < n; j++)
            if (i >= j)
                x[i][j] = x[i][j - 1] + x[i + 1][j] + x[i + 1][j - 1];
    return x;
}

int main()
{
    int n = 4, **x;
    x = matrice(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
            printf("%d ", x[i][j]);
        printf("\n");
    }
    return 0;
}
