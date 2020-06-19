#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

struct Edge
{
    int nod, cost;
};

vector<int> dijkstra(int k, int n, vector<vector<Edge>> adj)
{
    vector<int> d(n + 1, 9999);
    set<pair<int, int>> s;
    d[k] = 0;
    s.insert({ 0, k });
    for (int i = 1; i <= n; i++)
    {
        if (s.empty())
            break;
        int ind = (*s.begin()).second;
        s.erase(s.begin());
        for (auto edge: adj[ind])
            if (d[edge.nod] > d[ind] + edge.cost)
            {
                s.erase({ d[edge.nod], edge.nod });
                d[edge.nod] = d[ind] + edge.cost;
                s.insert({ d[edge.nod], edge.nod });
            }
    }
    return d;
}

int main()
{
    ifstream fin ("dijkstra.in");
    ofstream fout ("dijkstra.out");
    int n, m, k;
    fin >> n >> m >> k;

    vector<vector<Edge>> adj(n + 1);

    for (int i = 0; i < m; i++)
    {
        int a, b, cost;
        Edge k;
        fin >> a >> b >> cost;
        k.nod = b;
        k.cost = cost;
        adj[a].push_back(k);
    }

    vector<int> d(n + 1);
    d = dijkstra(k, n, adj);

    for (int i = 1; i <= n; i++)
        if (d[i] == 9999)
            fout << 0 << " ";
        else
            fout << d[i] << " ";

    return 0;
}
