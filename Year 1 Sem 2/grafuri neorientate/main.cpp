#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

void DFS(int node, vector<vector<int>> adj)
{
    static vector<bool> viz(100);
    viz[node] = 1;
    cout << node << " ";
    for (auto v : adj[node])
        if (viz[v] == 0)
            DFS(v, adj);
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
    for (i = 0; i < m; i++)
    {
        fin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cout << "Lista de adiacenta : " << endl;

    for (i = 1; i <= n; i++)///afisare lista de adiacenta
    {
        cout << i << ": ";
        for (auto j : adj[i])
            cout << j << " ";
        cout << endl;
    }

    cout << endl << "DFS: "; DFS(1, adj); cout << endl;

    cout << "BFS: "; BFS(1, adj); cout << endl;

    cout << endl;
    vector<int> k;
    k = distanta(1, n, adj);///face distanta de la un nod la celelalte

    for (int i = 1; i <= n; i++)
        cout << "Distanta de la " << 1 << " la " << i << " este : " << k[i] << endl;
    return 0;
}
