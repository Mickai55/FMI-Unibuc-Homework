#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    int n, m, a, b;
    ifstream fin ("sortaret.in");
    ofstream fout ("sortaret.out");
    fin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<int> intern(n + 1), viz(n + 1);
    queue<int> coada;
    for (int i = 0; i < m; i++)
    {
        fin >> a >> b;
        adj[a].push_back(b);
        intern[b]++;
    }
    for (int i = 1; i <= n; i++)
        if (intern[i] == 0)
            coada.push(i);
    while (!coada.empty())
    {
        fout << coada.front() << " ";
        int a = coada.front();
        coada.pop();
        for (auto i : adj[a])
        {
            intern[i]--;
            if (intern[i] == 0)
                coada.push(i);
        }
    }

    return 0;
}
