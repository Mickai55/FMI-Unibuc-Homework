#include <iostream>
#include <vector>
#include<typeinfo>
using namespace std;

class caca
{
public:
    int a;
    int b;
    caca (int a = 0, int b = 0)
    {
        this->a = a;
        this->b = b;
    }
    void operator= (caca &k)
    {
        a = k.a;
        b = k.b;
    }
};

int main()
{
    caca y(1, 2), z;
    z = y;
    cout << z.a;



    return 0;
}
