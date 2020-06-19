#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

void DFS(int node, vector<bool> &viz, vector<vector<int>> &adj)
{
    viz[node] = 1;
    cout << node << " ";
    for (auto v : adj[node])
        if (viz[v] == 0)
            DFS(v, viz, adj);
}

bool ciclu(int node, int parinte, vector<vector<int>> adj)
{
    static vector<bool> viz(100);
    viz[node] = 1;
    cout << node << " ";
    for (auto v : adj[node])
        if (viz[v] == 0)
        {
            if(ciclu(v, node, adj))
                return 1;
        }
        else if (parinte != v)
            return 1;
    return 0;
}


void BFS(int node, vector<vector<int>> adj)
{
    vector<bool> viz(100);
    queue<int> q;
    q.push(node);
    while (!q.empty())
    {
        int nod = q.front();
        viz[nod] = 1;
        cout << nod << " ";
        q.pop();
        for (auto vecin : adj[nod])
            if (viz[vecin] == 0)
                q.push(vecin);
    }
}

vector<int> distanta(int sursa, int n, vector<vector<int>> adj)
{
    vector<int> d(n + 1, n + 1);
    queue<int> q;
    d[sursa] = 0;
    q.push(sursa);
    while (!q.empty())
    {
        int nod = q.front();
        q.pop();
        for (auto vecin : adj[nod])
            if (d[vecin] > d[nod] + 1)
            {
                d[vecin] = d[nod] + 1;
                q.push(vecin);
            }
    }
    return d;
}

int main()
{
    ifstream fin ("date.in");
    int n, m, a, b, i;
    fin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<bool> viz(100);
    for (i = 0; i < m; i++)
    {
        fin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    DFS(1, viz, adj);

    return 0;
}
