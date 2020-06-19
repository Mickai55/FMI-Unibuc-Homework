#include <iostream>
using namespace std;
class A
{
    int x;
    public :
    int d()
    {
        cout << "plm";
        return x;
    }
};

int main()
{
    A a;int k;
    for (int i = 0; i < 100; i++)
        k = a.d();

  return 0;
}
