#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct Edge
{
    int nod, cost;
};

void DFS(int node, vector<bool> &viz, vector<vector<Edge>> &adj)
{
    viz[node] = 1;
    for (auto i : adj[node])
        if (viz[i.nod] == 0)
            DFS(i.nod, viz, adj);
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
    int sw = 1;
    for (int i = 1; i <= n; i++)
    {
        int s = 0;
        vector<bool> viz(n + 1, 0);
        DFS(i, viz, adj);
        for (int j = 1; j <= n - k; j++)
            if (viz[j] == 0)
                s++;
        if (s == n - k)
            sw = 0;
    }
    if (sw == 0)
        cout << "NU";
    else
        cout << "DA";

    return 0;
}
