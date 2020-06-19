#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int i,u=0,k=0,S=0,p=0,y=0,n,q,Max=0;
    char s[1000];
    cin.get(s,1000);
    n=strlen(s);
    da:
    i--;y=0;k=0;
    while (s[i]!='('||p==0){
        if (s[i]=='(')
            k++;
        if (s[i]==')'){
            y++;
            p=1;
        }
        i++;
        if (i==n)
            break;
    }
    if (y==k&&Max<y)
        y=Max;
    if (i<n)
        goto da;



    return 0;
}
