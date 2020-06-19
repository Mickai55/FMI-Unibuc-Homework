#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n,m,p,q,z,A[100],B[100],h=0,t[100],i,k=0,g=0,y[100],o=0,l[100],j,r=0;
    cin>>n>>m;
    cin>>p>>q;
    cin>>z;
    for (i=0;i<p;i++)
        cin>>A[i];
    for (i=0;i<q;i++)
        cin>>B[i];
    A[-1]=0;B[-1]=0;
    for (i=0;i<n;i++){
        if (i==A[k]){
            h++;
            t[h]=A[k]-A[k-1];
            k++;
        }
        if (i==n-1){
            h++;
            t[h]=i-A[k-1]+1;
        }
    }
    for (i=0;i<m;i++){
        if (i==B[r]){
            g++;
            y[g]=B[r]-B[r-1];
            r++;
        }
        if (i==m-1){
            g++;
            y[g]=i-B[r-1]+1;
        }
    }
    for (i=1;i<=g;i++)
        for (j=1;j<=h;j++){
            o++;
            l[o]=y[i]*t[j];
        }
    sort(l+1,l+o+1);
    cout<<l[o-z+1];

    return 0;
}
