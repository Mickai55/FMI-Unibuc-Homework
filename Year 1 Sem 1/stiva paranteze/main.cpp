#include <iostream>
using namespace std;

struct stiva{
    char info;
    stiva *trec;
}*varf=0;

void push (char x, stiva *&varf){
    stiva *s=varf,*p=varf;
    p=new stiva;
    p->info=x;
    if (p==0){
        p->trec=0;
        varf=p;
    }
    else{
        p->trec=s;
        varf=p;
    }
    s=p;
}

int pop (stiva *&varf){
    stiva *p=varf;
    varf=varf->trec;
    return p->info;
}

bool emty (stiva *varf){
    if (varf==0)
        return 0;
    return 1;
}


void afisare (){
    stiva *p=varf;
    while (p!=0){
        cout<<p->info;
        p=p->trec;
    }
}

int main()
{
    int n,ok=0;
    stiva *k;
    char x;
    cin>>n;
    for (int i=1;i<=n;i++){
        cin>>x;
        push(x, varf);
        if(varf->trec==NULL)
            continue;
        if (varf->info==')'&&varf->trec->info=='('){
            pop(varf);
            pop(varf);
        }
        if (varf)
        if (varf->info==')'){
            cout<<i-1;
            ok=1;
            break;
        }
    }
    if (ok==0)
        cout<<"E parantezat corect.";

    return 0;
}
