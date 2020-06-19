#ifndef AFD_H
#define AFD_H

#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
#include <iterator>

using namespace std;

class AFD
{
    public:
        // FUNCTII
        AFD(const int& x, const int& y);
        void check_if_well_defined();
        bool check_word (char c[]);
        friend std::ostream& operator << (ostream& out, AFD& afd);
        //COMPONENTELE AFD
        vector < vector < int > >  transition ;
        char* a; // Alfabetul de intrare
        bool* f; // Multimea Starilor Finale
        int nq; // Numarul de stari
        int na; // Numarul de cuvinte din alfabet
        int nt; // Numarul funtiilor de trazitie
    protected:
    private:

};

#endif // AFD_H
