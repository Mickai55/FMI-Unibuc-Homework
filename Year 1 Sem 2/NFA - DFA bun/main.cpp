#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <set>
#include <utility>
#include <queue>

#include <AFN.h>
#include <AFD.h>
using namespace std;

ifstream fin ("AFN.in");
ofstream fout ("AFD.out");

int main()
{
    AFN afn;
    fin >> afn;
    afn.turn_into_AFD();

    return 0;
}
