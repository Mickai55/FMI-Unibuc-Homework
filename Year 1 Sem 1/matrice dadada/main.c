#include <stdio.h>
#include <stdlib.h>

int* linie(int n, int k)
{
	int *x = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; i++)
		if (i % 2 == 0)
			x[i] = k;
		else
			x[i] = i;
	return x;

}


void Matrice(int *nrl, int *nrc, int *** y)
{
	scanf("%d%d", nrl, nrc);
	*y = (int**)malloc(*nrl * sizeof(int));
	for (int j = 0; j < *nrl; j++)
		(*y)[j] = linie(*nrc, j);

}

int main()
{
	int **y = NULL;
	int n, k;
	Matrice(&n, &k, &y);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < k; j++)
			printf("%d ", y[i][j]);
		printf("\n");
	}


	return 0;
}
