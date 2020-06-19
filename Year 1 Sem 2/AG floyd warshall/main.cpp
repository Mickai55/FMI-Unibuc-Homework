#include <fstream>
using namespace std;

ifstream fin("royfloyd.in");
ofstream fout("royfloyd.out");

int main()
{
    int n, m;
    fin >> n;
    int i, j, k;
    int a[n+1][n+1];
    for(i = 1; i <= n; i++)
        for(j = 1; j <= n; j++)
            fin >> a[i][j];

    for(k = 1; k <= n; k++)
        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
                if(a[i][k] != 0 && a[k][j] != 0 && i != j)
                    if (a[i][j] > a[i][k] + a[k][j] || a[i][j] == 0)
                        a[i][j] = a[i][k] + a[k][j];

    for(i = 1; i <= n; i++)
    {
        for(j = 1; j <= n; j++)
            fout << a[i][j] << " ";
        fout << "\n";
    }


}
