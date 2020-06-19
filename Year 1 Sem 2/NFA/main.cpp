#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

class NFA
{
    int q;          ///numar stari totale
    int *Q;         ///stari totale
    int f;          ///numar stari finale
    int *F;         ///stari finale
    int v;          ///numar litere
    char *V;        ///litere
    int g;          ///numar tranzitii
    struct tranz
    {
        int a, b;   ///tranzitii
        char c;
    }*G;
    int sc;         ///starea curenta
public:
    int I;          ///starea initiala
    int exista;
    int w;          ///numar cuvinte
    string *W;      ///cuvintele

    NFA(char *fisier)
    {
        int i;
        ifstream fin(fisier);
        fin >> q;
        Q = new int[q];
        for (i = 0; i < q; i++)
            fin >> Q[i];
        fin >> v;
        V = new char[v];
        for (i = 0; i < v; i++)
            fin >> V[i];
        fin >> I;
        fin >> f;
        F = new int[f];
        for (i = 0; i < f; i++)
            fin >> F[i];
        fin >> g;
        G = new tranz[g];
        for (i = 0; i < g; i++)
            fin >> G[i].a >> G[i].c >> G[i].b;
        fin >> w;
        W = new string [w];
        for (i = 0; i < w; i++)
            fin >> W[i];
        sc = 0;
        exista = 0;
    }
    bool verificare(string cuvant, int sc, int pozitia_in_cuvant);
};

bool NFA::verificare(string cuvant, int sc, int pozitia_in_cuvant)
{
    int i;
    if (pozitia_in_cuvant == cuvant.size())
    {
        for (i = 0; i < f; i++)
            if (sc == F[i])
            {
                exista = 1;
                return true;
            }
    }
    else
    {
        for (i = 0; i < g; i++)
            if (exista == 1)
                return true;
            else if ((G[i].a == sc) && (G[i].c == cuvant[pozitia_in_cuvant]))
                verificare(cuvant, G[i].b, pozitia_in_cuvant + 1);
        return false;
    }
}

int main()
{
    NFA automat1("date.in");
    for (int i = 0; i < automat1.w; i++)
    {
        if (automat1.verificare(automat1.W[i], automat1.I, 0) == true)
            cout << "Da" << endl;
        else
            cout << "Nu" << endl;
        automat1.exista = 0;
    }

    return 0;
}
