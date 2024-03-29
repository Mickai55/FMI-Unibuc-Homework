#include <fstream>
#include <iostream>
#include <string>
using namespace std;

ifstream fin("date.in");

int nrStari, nrAlfIn, nrAlfSt, nrFctTr, nrCuv;
char stari[100], stInit, alfIn[100], alfSt[100], simbInitSt, fctQ[100], fctIn[100], fctSt[100], fctQ2[100];
string cuv, fctSt2[100];

void citeste()
{
    int i;

    fin >> nrStari;
    for (i = 0; i < nrStari; i++)
        fin >> stari[i];

    fin >> nrAlfIn;
    for (i = 0; i < nrAlfIn; i++)
        fin >> alfIn[i];

    fin >> nrAlfSt;
    for (i = 0; i < nrAlfSt; i++)
        fin >> alfSt[i];

    fin >> stInit;
    fin >> simbInitSt;

    fin >> nrFctTr;
    for (i = 0; i < nrFctTr; i++)
        fin >> fctQ[i] >> fctIn[i] >> fctSt[i] >> fctQ2[i] >> fctSt2[i];
}

int acceptat(char stare, string cuv, string stiva)
{
    int j;
    string stiva2, s;
    if (cuv == "" && stiva == "")
        return 1;
    else
    {
        j = 0;
        while (j < nrFctTr)
        {
            if (fctIn[j] == '^')
            {
                if (stare == fctQ[j] && stiva[0]==fctSt[j])
                {
                    s = stiva.substr(1);
                    if (!(fctSt2[j] == "^"))
                        stiva2 = fctSt2[j];
                    else
                        stiva2 = "";
                    stiva2 += s;
                    if (acceptat(fctQ2[j], cuv, stiva2))
                        return 1;
                }
                if (stare == fctQ[j] && fctSt[j] == '^')
                {
                    s = stiva;
                    if (!(fctSt2[j] == "^"))
                        stiva2 = fctSt2[j];
                    else
                        stiva2 = "";
                    stiva2 += s;
                    if (acceptat(fctQ2[j], cuv, stiva2))
                        return 1;
                }
            }
            if (stare == fctQ[j] && cuv[0] == fctIn[j] && fctSt[j] == '^')
            {
                s = stiva;
                if (!(fctSt2[j] == "^"))
                    stiva2 = fctSt2[j];
                else
                    stiva2 = "";
                stiva2 += s;
                if (acceptat(fctQ2[j], cuv.substr(1), stiva2))
                    return 1;
            }
            if (stare == fctQ[j] && cuv[0] == fctIn[j] && stiva[0] == fctSt[j])
            {
                s = stiva.substr(1);
                if (fctSt2[j] != "^")
                    stiva2 = fctSt2[j];
                else
                    stiva2 = "";
                stiva2 += s;
                if (acceptat(fctQ2[j], cuv.substr(1), stiva2))
                    return 1;
            }
            j++;
        }
    }
    return 0;
}


int main ()
{
    citeste();

    fin >> nrCuv;
    for (int i = 0; i < nrCuv; i++)
    {
        fin >> cuv;
        string stiva;
        stiva = simbInitSt;
        if (acceptat(stInit, cuv, stiva))
            cout << cuv << " - acceptat\n";
        else
            cout << cuv << " - neacceptat\n";
    }


    return 0;
}
