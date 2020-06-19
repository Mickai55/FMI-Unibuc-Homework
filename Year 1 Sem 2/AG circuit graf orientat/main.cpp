#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct muchie
{
    int a, b;
};

void circuit(int nod, vector <muchie> v, int *viz, int *tata)
{
    viz[nod] = 1;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i].a == nod)
        {
            if (viz[v[i].b] == 0)
            {
                tata[v[i].b] = nod;
                circuit(v[i].b, v, viz, tata);
            }
            else
            {
                int ind = v[i].a;
                while (ind != v[i].b)
                {
                    if (ind == 0) ///????
                    return;
                    cout << ind << " ";
                    ind = tata[ind];
                }
                return;
            }
        }
    }
}

int main()
{
    int n, m;
    vector <muchie> muchii;
    muchie aux;
    int *viz, *tata;
    viz = new int [n + 1];
    tata = new int [n + 1];
    ifstream fin ("date.in");
    fin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        fin >> aux.a >> aux.b;
        muchii.push_back(aux);
    }
    circuit(1, muchii, viz, tata);

    return 0;
}
