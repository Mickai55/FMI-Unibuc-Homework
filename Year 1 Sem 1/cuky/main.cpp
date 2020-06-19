#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
    vector <int> x;
    int i,n,k,C,nr,pasi=0,p,u;
    while(x[0]<k&&x.size()>1)
    {
        u=0;
        C=x[0]+x[1]+x[1];
        x.erase(x.begin()+0,x.begin()+2);
        for (i=0; i<x.size(); i++)
            cout<<x[i]<<" ";
        cout<<endl;

        x.push_back(0);
        for (i=0;i<x.size();i++)
            if (C<x[i])
        {
            p=i;
            break;
        }
            else u++;

        if (u<x.size()){
        for (i=x.size()-1;i>=p;i--)
            x[i]=x[i-1];
        x[p]=C;
        }
        else
            x[x.size()-1]=C;

        for (i=0; i<x.size(); i++)
            cout<<x[i]<<" ";
        cout<<endl;
    }
    if(x.size()<=1)
        return -1;

    return pasi;
}
