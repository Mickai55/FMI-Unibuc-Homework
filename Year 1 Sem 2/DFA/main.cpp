#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void verif (string k, int I, int D[][256], int f, int F[100])
{
    int sa = I;
    for (int i = 0; i < k.size(); i++)
        sa = D[sa][k[i]];
    for (int i = 0; i < f; i++)
        if (sa == F[i])
        {
            cout << "DA" << endl;
            return;
        }
    cout << "NU" << " ";

}

int main()
{
    int q, i, j, e, I, f, d, x, z, c;
    char y;
    ifstream fin ("date.in");
    fin >> q; /// q - stari totale
    int Q[q];
    for (i = 0; i < q; i++)
        fin >> Q[i];
    fin >> e; /// e - numar de litere
    char E[e];
    for (i = 0; i < e; i++)
        fin >> E[i];
    fin >> I; /// starea initiala
    fin >> f; /// f - stari finale
    int F[f];
    for (i = 0; i < f; i++)
        fin >> F[i];
    fin >> d; /// d - numar de tranzitii
    int D[q+1][256] = {0};
    for (i = 0; i < d; i++)
    {
        fin >> x >> y >> z; /// 1 a 2
         D[x][y] = z;/// D[1][a] = 2
    }
    fin >> c;
    string *C;
    C = new string [c];
    for (i = 0; i < c; i++)
    {
        fin >> C[i];
        verif(C[i], I, D, f, F);
    }


    return 0;
}
