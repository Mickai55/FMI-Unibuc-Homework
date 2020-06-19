#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
    ifstream fin ("date.in");
	ofstream fout ("date.out");
void DFS(int node, vector<vector<int>> &adj, vector<bool> &viz)
{
    viz[node] = 1;
    for (auto v : adj[node])
        if (viz[v] == 0)
            DFS(v, adj, viz);
}

int main()
{

    int n, i, j, nr = 0;
    fin >> n;
    vector<vector<int>> adj(n + 1);
    int x[n + 1], y[n + 1];
    for (i = 1; i <= n; i++)
        fin >> x[i] >> y[i];
    for (i = 1; i < n; i++)
        for (j = i + 1; j <= n; j++)
            if (x[i] == x[j] || y[i] == y[j])
            {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }

    vector<bool> viz(n + 1);

    for (i = 1; i <= n; i++)
        if (viz[i] == 0)
        {
            DFS(i, adj, viz);
            nr++;
        }
    fout << nr - 1;

    return 0;
}
