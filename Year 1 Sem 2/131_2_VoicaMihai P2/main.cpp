#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

struct Edge
{
    int nod, cost;
};

vector<int> dijkstra(int k, int n, vector<vector<Edge>> &adj)
{
    vector<int> d(n + 1, 100);
    set<pair<int, int>> s;
    s.insert({ 0, k });
    d[k] = 0;
    for (int i = 1; i <= n; i++)
    {
        while (!s.empty())
        {
            int ind = (*s.begin()).second;
            s.erase(s.begin());
            for (auto edge : adj[ind])
                if (d[edge.nod] > edge.cost + d[ind])
                {
                    s.erase({d[edge.nod], edge.nod});
                    d[edge.nod] = edge.cost + d[ind];
                    s.insert({d[edge.nod], edge.nod});
                }
        }
    }
    return d;
}

int main()
{
    ifstream fin ("date.in");
    int n, m, k, a, b, c;
    fin >> n >> m >> k;
    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; i++)
    {
        fin >> a >> b >> c;
        Edge y;
        y.nod = b;
        y.cost = c;
        adj[a].push_back(y);
        y.nod = a;
        adj[b].push_back(y);
    }
    vector<int> T(n + 1, 100);
    vector<int> ind(n + 1);
    vector<int> f(n - k + 1);
    for (int i = 1; i <= n - k; i++)
    {
        T[i] = i;
        f[i] = i;
    }
    for (int i = 1; i <= n - k; i++)
    {
        vector<int> d = dijkstra(i, n, adj);
        for (int j = 1; j <= n; j++)
            if (T[j] > d[j])
            {
                T[j] = d[j];
                ind[j] = i;
            }
    }
    for (int i = 1; i <= n; i++)
        cout << ind[i] << " ";

    return 0;
}
