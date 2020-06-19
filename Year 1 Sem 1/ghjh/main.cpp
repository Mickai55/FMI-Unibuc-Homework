#include <iostream>
using namespace std;
void pula (int i){
    if (i<10)
    pula(++i);
    cout<<i<<" ";
}

int main()
{
    pula(0);

    return 0;
}
