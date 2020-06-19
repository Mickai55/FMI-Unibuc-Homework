#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

struct Edge
{
    int nod, cost;
};

int main()
{
    ifstream fin ("dijkstra.in");
    ofstream fout ("dijkstra.out");
    int n, m;
    fin >> n >> m;
    vector<int> d(n + 1, (n - 1) * 20000);
    vector<int> viz(n + 1, 0);
    vector<vector<Edge>> G(n + 1);
    set<pair<int, int>> s;
    d[1] = 0;
    s.insert(make_pair(0, 1));
    for (int i = 0; i < m; i++)
    {
        int a, b, cost;
        Edge k;
        fin >> a >> b >> cost;
        k.nod = b;
        k.cost = cost;
        G[a].push_back(k);
    }
    for (int i = 1; i <= n; i++)
    {
        if (s.empty())
            break;
        int ind = (*s.begin()).second;
        s.erase(s.begin());
        for (auto edge: G[ind])
        {
            if (d[edge.nod] > d[ind] + edge.cost)
            {
                s.erase(make_pair(d[edge.nod], edge.nod));
                d[edge.nod] = d[ind] + edge.cost;
                s.insert(make_pair(d[edge.nod], edge.nod));
            }
        }

    }

    for (int i = 2; i <= n; i++)
            fout << d[i] << " ";

    return 0;
}
