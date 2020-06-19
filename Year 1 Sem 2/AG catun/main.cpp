#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

struct Edge
{
    int nod, cost;
};

int main()
{
    ifstream fin("catun.in");
    ofstream fout("catun.out");
    int n, m, k, a, b, c;
    fin >> n >> m >> k;
    vector<int> fort(k);
    vector<vector<Edge>> adj(n + 1);

    set<pair<int, int>> s;

    for (int i = 0; i < k; i++)
        fin >> fort[i];
    for (int i = 0; i < m; i++)
    {
        fin >> a >> b >> c;
        Edge q;
        q.nod = b;
        q.cost = c;
        adj[a].push_back(q);
        q.nod = a;
        adj[b].push_back(q);
    }
    vector<int> valoare(n + 1, 36000);
    vector<int> nod(n + 1);
    for (int j = 0; j < k; j++)
    {
        s.insert(make_pair(0, fort[j]));
        vector<int> d(n + 1, 36000);
        d[fort[j]] = 0;
        for (int i = 1; i <= n; i++)
        {
            if (s.empty())
                break;
            int ind = (*s.begin()).second;
            s.erase(s.begin());
            for (auto edge: adj[ind])
                if (d[edge.nod] > d[ind] + edge.cost)
                {
                    s.erase(make_pair(d[edge.nod], edge.nod));
                    d[edge.nod] = d[ind] + edge.cost;
                    s.insert(make_pair(d[edge.nod], edge.nod));
                }
        }
        for (int i = 1; i <= n; i++)
            if (d[i] < valoare[i] && find(fort.begin(), fort.end(), i) == fort.end())
            {
                valoare[i] = d[i];
                nod[i] = fort[j];
            }
    }
    for (int i = 1; i <= n; i++)
        fout << nod[i] << " ";
    fin.close();
    fout.close();


    return 0;
}
