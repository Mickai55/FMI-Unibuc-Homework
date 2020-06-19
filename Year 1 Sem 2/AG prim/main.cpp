#include <fstream>
#include <vector>
#include <set>
using namespace std;
ifstream fin("apm.in");
ofstream fout("apm.out");
int main()
{
	int n, m;
	fin >> n >> m;
	vector <vector <pair <int, int> > > adj(n+1);
	vector <int> viz(n + 1, 0), d(n + 1, INT_MAX), t(n + 1, 0);
	set <pair <int, int> > S;
	for (int i = 1; i <= m; i++)
    {
		int x, y, cost;
		fin >> x >> y >> cost;
		adj[x].push_back({ cost,y });
		adj[y].push_back({ cost,x });
	}
	S.insert({ 0,1 });
	d[1] = 0;

	while (!S.empty())
    {
		int nod = S.begin()->second;
		viz[nod] = 1;
		S.erase(S.begin());
		for (auto i : adj[nod])
			if (viz[i.second] == 0 && i.first < d[i.second])
            {
				d[i.second] = i.first;
				S.insert({d[i.second], i.second});
				t[i.second] = nod;
			}
	}
	int cost = 0;
	for (int i = 1; i <= n; i++)
		cost += d[i];
	fout << cost << '\n' << n - 1 << '\n';
	for (int i = 2; i <= n; i++)
		fout << i << ' ' << t[i]<< '\n';


    return 0;
}
