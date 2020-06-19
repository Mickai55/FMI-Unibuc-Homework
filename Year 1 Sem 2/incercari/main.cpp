#include <iostream>
using namespace std;

class punct
{
    int x, y;

public:
    void citDirect (int a, int b)
    {
        x = a;
        y = b;
    }
    void citTast ()
    {
        int a, b;
        cin >> a >> b;
        x = a;
        y = b;
    }
    void afis()
    {
        cout << x << " " << y;
    }
};

int main()
{
    punct A;
    A.citTast();
    A.afis();


    return 0;
}
