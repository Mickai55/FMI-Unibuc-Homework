#include <iostream>
using namespace std;
struct vec{
    int val,ind;
    vec *urm;
};
vec *primv1,*ultimv1,*primv2,*ultimv2;
int n,m;

void creare (int k, vec *&prim, vec *&ultim){
    int i,x;
    vec *p;
    for (i=1;i<=k;i++){
        cin>>x;
        if (x!=0){
            p=new vec;
            p->val=x;
            p->ind=i;
            p->urm=NULL;
            if (prim==NULL){
                prim=ultim=p;
            }
            else{
                ultim->urm=p;
                ultim=p;
            }
        }
    }
}

void afisare (vec *prim){
    vec *p;
    p=prim;
    while (p!=NULL){
        cout<<p->ind<<"-"<<p->val<<" ";
        p=p->urm;
    }
    cout<<endl;
}

void suma (){
    int i;
    vec *p=primv1,*q=primv2;
    if (n>m)
        for (i=1;i<=n;i++){
            if (p->val!=0&&q->val!=0)
                cout<<p->ind<<"-"<<p->val+q->val<<" ";
                else if (p->val!=0&&q->val==0)
                    cout<<p->ind<<"-"<<p->val<<" ";
                else
                    cout<<q->ind<<"-"<<q->val<<" ";
            p=p->urm;
            q=q->urm;
        }
}

int main()
{
    cin>>n;
    creare(n,primv1,ultimv1);
    cin>>m;
    creare(m,primv2,ultimv2);
    suma();

    return 0;
}
