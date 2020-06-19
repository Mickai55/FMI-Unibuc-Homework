#include <bits/stdc++.h>

using namespace std;
ifstream in("graf.in");
ofstream out("graf.out");
vector<int> v[7505];
bool viz[7505];
int distx[7505],disty[7505],rez[7505];
void BFS(int x, int dist[])
{
    queue<int> q;
    q.push(x);
    memset(viz,0,sizeof(viz));
    viz[x] = 1;
    while(!q.empty())
    {
        int now = q.front();
        for (auto it: v[now])
            if (!viz[it])
            {
                viz[it] = 1;
                dist[it] = 1+dist[now];
                q.push(it);
            }
        q.pop();
    }
}
int main()
{
    int n,m,x,y;
    in >> n >> m >> x >> y;
    for (int i = 1; i<=m; i++)
    {
        int a,b;
        in >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    BFS(x,distx);
    BFS(y,disty);
    int cnt = 0;
    for (int i = 1; i<=n; i++)
        if (distx[i]+disty[i] == distx[y])
        {
            if (rez[distx[i]]>0)
                rez[distx[i]] = -1;
            else if (!rez[distx[i]])
                rez[distx[i]] = i;
        }
    for (int i = 0; i<=distx[y]; i++)
        cnt+=(rez[i]>0);
    out << cnt << "\n";
    sort(rez,rez+distx[y]+1);
    for (int i = 0; i<=distx[y]; i++)
        if (rez[i]>0)
            out << rez[i] << " ";
}
