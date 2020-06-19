#include<fstream>
#include<iomanip>
#include<cmath>
using namespace std;

ifstream fin("retea2.in");
ofstream fout("retea2.out");

int n,m,poz;
long long Min,dist[10000];

struct punct
{
    long long x,y;

} a[10000];

long double sol;
int main()
{
    fin>>n>>m;
    for(int i=1; i<=n+m; ++i)
    {
        fin>>a[i].x>>a[i].y;
    }
    dist[1]=-1;

    for(int i=n+1; i<=n+m; ++i)
    {
        dist[i]=(a[1].x-a[i].x)*(a[1].x-a[i].x)+(a[1].y-a[i].y)*(a[1].y-a[i].y);
    }
    for(int i=2; i<=n+m; ++i)
    {
        Min=10000000000000.00;
        for(int j=2; j<=n+m; ++j)
        {
            if(Min>dist[j]&&dist[j]!=-1)
            {
                Min=dist[j];
                poz=j;
            }
        }
        dist[poz]=-1;
        sol=sol+sqrt(Min);
        for(int j=2; j<=n+m; ++j)
        {
            dist[j]=min(dist[j],(a[poz].x-a[j].x)*(a[poz].x-a[j].x)+(a[poz].y-a[j].y)*(a[poz].y-a[j].y));
        }
    }
    fout<<fixed<<setprecision(7)<<sol;
}
