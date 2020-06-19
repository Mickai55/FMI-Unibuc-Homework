#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

struct muchie
{
	int a, b, cost;
};

void DFS(int node, vector<int> &viz, vector<vector<int>> &adj)
{
	viz[node] = 1;
	for (auto v : adj[node])
		if (viz[v] == 0)
			DFS(v, viz, adj);
}

bool verifica(int a, int b, int n, vector<vector<int>> &adj)
{
	vector<int> viz(n + 1, 0);
	DFS(a, viz, adj);
	return !viz[b];
}

bool cmp(muchie a, muchie b)
{
	return a.cost < b.cost;
}

int main()
{
	int n, m, i = 0;
	ifstream fin("apm.in");
	ofstream fout ("apm.out");
	fin >> n >> m;
	vector<vector<int>> adj(n + 1);
	int a[n], b[n];
	vector<muchie> muchii(m);
	for (int i = 0; i < m; i++)
		fin >> muchii[i].a >> muchii[i].b >> muchii[i].cost;

	sort(muchii.begin(), muchii.end(), cmp);

	int cost_total = 0;
	for (auto muchie : muchii)
		if (verifica(muchie.a, muchie.b, n, adj))
		{
			cost_total += muchie.cost;
			adj[muchie.a].push_back(muchie.b);
			adj[muchie.b].push_back(muchie.a);
			a[i] = muchie.a; b[i] = muchie.b;
			i++;
		}
	fout << cost_total << "\n" << n - 1 << "\n";
    for (i = 0; i < n - 1; i++)
        fout << b[i] << " " << a[i] << "\n";

    return 0;
}
