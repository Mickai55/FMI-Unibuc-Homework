#include <stdio.h>
#include <stdlib.h>

void vector (int *n, int **x)
{
    scanf ("%d",n);
    *x = (int*) malloc (*n * sizeof(int));
    for (int i=0; i<*n; i++)
        scanf("%d",&(*x)[i]);
}

int main()
{
    int n,*x;
    vector (&n,&x);
    for (int i=0; i<n; i++)
        printf("%d ",x[i]);


    return 0;
}
