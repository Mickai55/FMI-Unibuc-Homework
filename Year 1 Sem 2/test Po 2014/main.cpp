#include <iostream>
#include <vector>
using namespace std;

struct Data
{
    int zi, luna, an;
};

class Adult
{
public:
    string nume;
    string prenume;
    int varsta;
    string adresa;
    int col;
    int tensiune;
    Data data_tensiune;
    Data data_colesterol;
    int risc_cardiovascular = -1;

public:

    Adult(string nume = "da", string prenume = "da", int varsta = -1, string adresa = "da", int col = -1, int tensiune = -1, int zicol = -1,
          int lunacol = -1, int ancol = -1, int ziten = -1, int lunaten = -1, int anten = -1)
    {
        this->nume = nume;
        this->prenume = prenume;
        this->varsta = varsta;
        this->adresa = adresa;
        this->col = col;
        this->tensiune = tensiune;
        this->data_colesterol.zi = zicol;
        this->data_colesterol.luna = lunacol;
        this->data_colesterol.an = ancol;
        this->data_tensiune.zi = ziten;
        this->data_tensiune.luna = lunaten;
        this->data_tensiune.an = anten;
    }

    void operator= (Adult k)
    {
        nume = k.nume;
        prenume = k.prenume;
        varsta = k.varsta;
        adresa = k.adresa;
        col = k.col;
        tensiune = k.tensiune;
        data_colesterol = k.data_colesterol;
        data_tensiune = k.data_tensiune;
    }

    void afisare_adult()
    {
        cout << nume << " " << prenume << " " << varsta << " " << adresa << " " << col << "(" << data_colesterol.zi << "," << data_colesterol.luna
         << "," << data_colesterol.an << ")" << " " << tensiune << "(" << data_tensiune.zi << "," << data_tensiune.luna
         << "," << data_tensiune.an << ")" << "\n";
        if (this->risc_cardiovascular == -1)
            cout << "NEVERIFICAT" << " ";
         else if (this->risc_cardiovascular == 0)
            cout << "E SANATOS TUN" << " ";
         else if (this->risc_cardiovascular == 1)
            cout << "E PE MOARTE" << " ";
         else if (this->risc_cardiovascular > 1)
            cout << "E MORT" << " ";

    }

    virtual void afis()
    {
        afisare_adult();
    }

    friend ostream& operator<<(ostream &out, Adult &k)
    {
        k.afis();
        return out;
    }

    friend istream& operator>>(istream &in, Adult &k)
    {
        in >> k.nume >> k.prenume >> k.varsta >> k.adresa >> k.col >> k.tensiune;
        return in;
    }

};

class Adult40 : public Adult
{public:
    bool fumator;
    string sedentarism;



    Adult40(string nume = "da", string prenume = "da", int varsta = -1, string adresa = "da", int col = -1, int tensiune = -1, int zicol = -1,
          int lunacol = -1, int ancol = -1, int ziten = -1, int lunaten = -1, int anten = -1, bool fumator = 0, string sedentarism = "da")
    : Adult(nume, prenume, varsta, adresa, col, tensiune, zicol, lunacol, ancol, ziten, lunaten, anten)
    {
        this->fumator = fumator;
        this->sedentarism = sedentarism;
    }

    void operator= (Adult40 k)
    {
        nume = k.nume;
        prenume = k.prenume;
        varsta = k.varsta;
        adresa = k.adresa;
        col = k.col;
        tensiune = k.tensiune;
        data_colesterol = k.data_colesterol;
        data_tensiune = k.data_tensiune;
        fumator = k.fumator;
        sedentarism = k.sedentarism;
    }

    void afis()
    {
        afisare_adult();
        cout << fumator << " " << sedentarism << "\n";
    }

    friend istream& operator>>(istream &in, Adult40 &k)
    {
        in >> (Adult&) k;
        in >> k.fumator >> k.sedentarism;

        return in;
    }

};

class Copil : public Adult
{
    int boli_parinti;
    string numep1, prenumep1, numep2, prenumep2;

public:

    Copil(string nume = "da", string prenume = "da", int varsta = -1, string adresa = "da", int col = -1, int tensiune = -1, int zicol = -1,
          int lunacol = -1, int ancol = -1, int ziten = -1, int lunaten = -1, int anten = -1,
          int boli_parinti = -1, string numep1 = "da", string prenumep1 = "da", string numep2 = "da", string prenumep2 = "da")
    : Adult(nume, prenume, varsta, adresa, col, tensiune, zicol, lunacol, ancol, ziten, lunaten, anten)
    {
        this->boli_parinti = boli_parinti;
        this->numep1 = numep1;
        this->prenumep1 = prenumep1;
        this->numep2 = numep2;
        this->prenumep2 = prenumep2;
    }

    void operator= (Copil k)
    {
        nume = k.nume;
        prenume = k.prenume;
        varsta = k.varsta;
        adresa = k.adresa;
        col = k.col;
        tensiune = k.tensiune;
        data_colesterol = k.data_colesterol;
        data_tensiune = k.data_tensiune;
        boli_parinti = k.boli_parinti;
        numep1 = k.numep1;
        prenumep1 = k.prenumep1;
        numep2 = k.numep2;
        prenumep2 = k.prenumep2;
    }

    void afis()
    {
        afisare_adult();
        cout << boli_parinti << " " << numep1 << " " << prenumep1 << " " << numep2 << " " << prenumep1 << "\n";
    }

    friend istream& operator>>(istream &in, Copil &k)
    {
        in >> (Adult&) k;
        in >> k.boli_parinti >> k.numep1 >> k.prenumep1 >> k.numep2 >> k.prenumep2;

        return in;
    }

};

template<typename T>
class Consultatie
{
public:
    vector<T> pacienti;
    static int Nr;

    void adaugare(T k)
    {
        pacienti.push_back(k);
        Nr++;
    }

    void afisare_pacienti()
    {
        for(auto i : pacienti)
            cout << i << "\n";
    }

    void risc()
    {
        typename vector<T>::iterator i;
        for(i = pacienti.begin(); i != pacienti.end(); i++)
        {
            if ((*i).col > 240)
                (*i).risc_cardiovascular++;
            if ((*i).tensiune < 130 || (*i).tensiune > 139)
                (*i).risc_cardiovascular++;
            if ((*i).fumator == 1)
                (*i).risc_cardiovascular++;
            if ((*i).sedentarism == "scazut")
                (*i).risc_cardiovascular++;
        }
    }

    void stergere(T k)
    {
        typename vector<T>::iterator i;
        for(i = pacienti.begin(); i != pacienti.end(); i++)
            if ((*i).nume == k.nume)
                pacienti.erase(i);
    }

};

template<typename T> int Consultatie<T>::Nr = 0;

int main()
{
    Adult40 a("coyz", "andrei", 69, "bucuresti", 500, 123, 11, 9, 1999, 1, 1, 1989, 0, "scazu"), b;
    //Copil q("coyz", "andrei", 69, "bucuresti", 500, 123, 11, 9, 1999, 1, 1, 1989, 2), y;
    Consultatie<Adult40> con;
    con.adaugare(a); con.adaugare(b);
    con.stergere(a);
    con.afisare_pacienti();

    return 0;
}
