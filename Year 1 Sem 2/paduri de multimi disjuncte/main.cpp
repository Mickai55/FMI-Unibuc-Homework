#include <stdio.h>

#define NMAX 100020

int TT[NMAX], RG[NMAX];
int N, M;

int find(int x)
{
	int R, y;

	//merg in sus pe arbore pana gasesc un nod care pointeaza catre el insusi
	for (R = x; TT[R] != R; R = TT[R]);

	//aplic compresia drumurilor
	for (; TT[x] != x;)
	{
		y = TT[x];
		TT[x] = R;
		x = y;
	}
	return R;
}

void unite(int x, int y)
{
	//unesc multimea cu rang mai mic de cea cu rang mai mare
	if (RG[x] > RG[y])
		TT[y] = x;
			else TT[x] = y;

	//in caz ca rangurile erau egale atunci cresc rangul noii multimi cu 1
	if (RG[x] == RG[y]) RG[y]++;
}

int main()
{
	freopen("disjoint.in", "r", stdin);
	freopen("disjoint.out", "w", stdout);

	scanf("%d %d ", &N, &M);

	int i, x, y, cd;

	//initial fiecare nod pointeaza catre el insusi iar rangul fiecarui arbore este 1
	for (i = 1; i <= N; i++)
	{
		TT[i] = i;
		RG[i] = 1;
	}

	for (i = 1; i <= M; i++)
	{
		scanf("%d %d %d", &cd, &x, &y);

		if (cd == 2){
			//verific daca radacina arborilor in care se afla x respectiv y este egala
			if (find(x) == find(y)) printf("DA\n");
				else printf("NU\n");
		}
			else //unesc radacinile arborilor corespunzatori multimilor nodurilor x respectiv y
				{
					if (find(x) == find(y))	 {fprintf(stderr,"%d ", i);return 0;}
					unite(find(x), find(y));
				}
	}

	return 0;
}
