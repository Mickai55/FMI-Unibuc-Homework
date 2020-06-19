#include <iostream>
#include <vector>
using namespace std;

class Adult
{
protected:
    string nume;
    string prenume;
    int varsta;
    string adresa;
    int col;
    int tensiune;

public:

    Adult(string nume = "da", string prenume = "da", int varsta = -1, string adresa = "da", int col = -1, int tensiune = -1)
    {
        this->nume = nume;
        this->prenume = prenume;
        this->varsta = varsta;
        this->adresa = adresa;
        this->col = col;
        this->tensiune = tensiune;
    }

    void operator= (Adult k)
    {
        nume = k.nume;
        prenume = k.prenume;
        varsta = k.varsta;
        adresa = k.adresa;
        col = k.col;
        tensiune = k.tensiune;
    }

    void afisare_adult()
    {
        cout << nume << " " << prenume << " " << varsta << " " << adresa << " " << col << " " << tensiune;
    }

    virtual void afis()
    {
        afisare_adult();
    }

};

int main()
{



    return 0;
}
