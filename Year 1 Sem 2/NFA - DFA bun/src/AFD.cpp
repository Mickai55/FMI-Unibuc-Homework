#include "AFD.h"

#define MAX_STATE INT_MAX
#define MAX_SYMBOL INT_MAX

AFD::AFD(const int& x, const int& y)
{
    if (x > MAX_STATE || y > MAX_SYMBOL)
    {
        cout << "OVERFLOW";
        exit (0);
    }
    a = new char [y+1];
    f = new bool [x];
    transition.resize (x);
    for (int i = 0; i < x; i++)
    {
        f[i] = false;
        transition[i].resize (y);
        // Initial matricea nu indica nici o stare
        for (int j = 0; j < y; j++)
            transition[i][j] = -1;
    }
    na  = y;
    nq  = x;
    nt  = 0;
}

std::ostream& operator << (ostream& out, AFD& afd)
{
    ofstream fout ("date.out");
    int ind = 0, nf = 0, nrt = 0;
    fout << afd.nq << '\n';
    for (int i = 1; i <= afd.nq; i++)
        fout << i << " ";
    fout << '\n';
    fout << afd.na << '\n';
    for (int i = 0; i < afd.na; i++)
        fout << afd.a[i] << " ";
    fout << '\n';

    fout << 1 << '\n';

    for (int i = 0; i < afd.nq; i++)
        if (afd.f[i] == true)
            nf++;
    fout << nf << '\n';
    for (int i = 0; i < afd.nq; i++)
        if (afd.f[i] == true)
            fout << i + 1 << " ";
    fout << "\n";
    for (int i = 0; i < afd.nq ; i++)
        for (int j = 0; j < afd.na ; j++)
            if (afd.transition[i][j] != -1)
                nrt++;
    fout << nrt << '\n';
    for (int i = 0; i < afd.nq ; i++)
    {
        for (int j = 0; j < afd.na ; j++)
            if (afd.transition[i][j] != -1)
                fout << ind + 1 << " " << afd.a[j] << " " << afd.transition[i][j] + 1 << "\n";
        ind++;
    }

    return fout;
}
