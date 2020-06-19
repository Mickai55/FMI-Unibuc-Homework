#include <iostream>
#include <math.h>
using namespace std;

class punct
{
private:
    int x, y;
public:
    punct();
    punct(int);
    punct(int, int);
    ~punct();
    afis();
    float distanta(punct);

    punct operator + (punct K)
    {
        punct *A;
        A = new punct(K.x + x, K.y + y);
        return *A;
    }

};



float punct::distanta(punct K)
{
    return sqrt((K.x - x) * (K.x - x) + (K.y - y) * (K.y - y));
}

punct::afis()
{
    cout << x << " " << y;
}

punct::punct()
{
    x = 0;
    y = 7;
}

punct::punct(int a)
{
    x = a;
    y = 7;
}

punct::punct(int a, int b)
{
    x = a;
    y = b;
}

punct::~punct()
{
    x = y = 0;
}

int main()
{
    punct A(1, 1), B(8, 3), C(0, 0), L(1, 1);
    punct D(C);
    punct E = D;
    punct F;
    F = A + B;
    F.afis();

    return 0;
}
