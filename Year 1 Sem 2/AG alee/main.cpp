#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    ifstream fin ("alee.in");
    ofstream fout ("alee.out");
    int n, m, x1, y1, x2, y2, s, f, a, b;

    fin >> n >> m;
    vector<int> k(m + 1);
    for (int i = 0; i < m; i++)
    {
        fin >> a >> b;
        k[i] = (a - 1) * n + b;
    }
    fin >> x1 >> y1 >> x2 >> y2;

    s = (x1 - 1) * n + y1;
    f = (x2 - 1) * n + y2;

    vector<vector<int>> adj(n * n + 1);

    for (int i = 1; i < n * n; i++)
        if (i % n != 0 && find(k.begin(), k.end(), i) == k.end())
        {
            adj[i].push_back(i + 1);
            adj[i + 1].push_back(i);
        }
    for (int i = 1; i <= n * (n - 1); i++)
        if (find(k.begin(), k.end(), i) == k.end())
        {
            adj[i].push_back(i + n);
            adj[i + n].push_back(i);
        }
    vector<int> d(n * n + 1, n * n + 1);
    queue<int> q;
    d[s] = 1;
    q.push(s);
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

    fout << d[f];




    // for (int i = 1; i <= n * n; i++)
    // {
    //     cout << i << ":";
    //     for (auto j : adj[i])
    //         cout << j << " ";
    //     cout << endl;
    // }


    return 0;
}
