#include <iostream>
using namespace std;
class A
{
    public:
    static int x;
public:
A(int i=0);

    int get_x()
    {
        return x;
    }
    int& set_x(int i)
    {
        x=3;
    }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
A::A(int i)
    {
        A::x=i;
    }
int main()
{
    A a(212), b;/// a.x = 212, b.x = 0
    cout<<(b=a).get_x();

    int k;
    double l;
    k = l;

    return 0;
}
