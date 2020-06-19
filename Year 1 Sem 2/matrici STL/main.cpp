#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector < vector <int> > Mat(3, vector < int >(3));
    int i, j;
    for (i = 0; i < 6; i++)
    {
        for (j = 0; j < 6; j++)
            cout << Mat[i][j] << " ";
        cout << endl;
    }
    for (auto x:Mat)
    {
        for(auto y : x)
            cout << y << " ";
        cout << endl;
    }


    return 0;
}
