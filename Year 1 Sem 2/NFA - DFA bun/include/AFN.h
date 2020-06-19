#ifndef AFN_H
#define AFN_H

#include <iostream>
#include <fstream>
#include <cstring>
#include <string.h>
#include <set>
#include <vector>
#include <iterator>
#include <math.h>
#include <queue>

#include <AFD.h>

using namespace std;

class AFN
{
    private:
         vector < vector < set < int > > > transition; //Functia de tranzitie
         char* a; // Alfabetul de intrare
         bool* f; // Multimea Starilor Finale
         int nq; // Numarul de stari
         int na; // Numarul de cuvinte din alfabet
         int nt; // Numarul funtiilor de trazitie
         int sf; // Numarul de stari finale
         int *SF; //Starile finale
         int si; //starea initiala
         int *vect;
     public:
        AFN();
        AFD& turn_into_AFD ( );//Functia de transformare AFN -> AFD
        friend std::istream& operator>>(std::istream& in,AFN& afn);
        friend std::ostream& operator<<(std::ostream& out,AFN& afn);

};

#endif // AFN_H
