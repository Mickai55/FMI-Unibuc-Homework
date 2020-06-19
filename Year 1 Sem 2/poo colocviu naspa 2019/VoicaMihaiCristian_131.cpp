#include <iostream>
#include <vector>
#include <typeinfo>
#include <string.h>
#include <algorithm>
using namespace std;

class Statie
{
public:
    string nume;
    string strada;
    int numar;
    int sector;
    vector<int> lista;
    static int cod;

    Statie(string nume = "a", string strada = "b", int numar = -1, int sector = -1, vector<int> lista = {})
    {
        this->nume = nume;
        this->strada = strada;
        this->numar = numar;
        this->sector = sector;
        this->lista = lista;
        cod++;
    }

    void operator= (Statie k)
    {
        nume = k.nume;
        strada = k.strada;
        numar = k.numar;
        sector = k.sector;
        lista = k.lista;
    }

    void afisare_statie()
    {
        cout << "Statia " << nume << "\n";
        cout << "Strada: " << strada << "\n";
        cout << "Numar: " << numar << "\n";
        cout << "Sector: " << sector << "\n";
        cout << "Lista autobuze : ";
        for (auto i : lista)
            cout << i << " ";
    }

    virtual void afis()
    {
        afisare_statie();
        cout << "\n";
    }

    friend ostream& operator<<(ostream &out, Statie &k)
    {
        k.afis();
        return out;
    }

    friend istream& operator>>(istream &in, Statie &k)
    {
        int n, x;
        in >> k.nume >> k.strada >> k.numar >> k.sector >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> x;
            k.lista.push_back(x);
        }
    }

};

int Statie::cod = 0;

class SU : public Statie
{
    bool legitimatii;
    string obiectiv;

public:

    SU(string nume = "a", string strada = "b", int numar = -1, int sector = -1, vector<int> lista = {}, bool legitimatii = 0, string obiectiv = "")
    : Statie (nume, strada, numar, sector, lista)
    {
        this->legitimatii = legitimatii;
        this->obiectiv = obiectiv;

        try
        {
            if (legitimatii !=0 && legitimatii !=1)
            throw(1);
        }
        catch(int d)
        {
            cout << "Introduceti 1 daca exista statie de legitimatii si 0 daca nu!";
            exit(0);
        }
    }

    void operator= (SU k)
    {
        nume = k.nume;
        strada = k.strada;
        numar = k.numar;
        sector = k.sector;
        lista = k.lista;
        legitimatii = k.legitimatii;
        obiectiv = k.obiectiv;
    }

    void afis()
    {
        afisare_statie();
        cout << "\n";
        if (legitimatii == 1)
            cout << "Are punct de achizitionare de legitimatii." << "\n";
        else
            cout << "Nu are punct de achizitionare de legitimatii." << "\n";
        if (obiectiv == "")
            cout << "Nu are obiective turistice in apropiere." << "\n";
        else
            cout << "Obiectiv turistic: " << obiectiv << "\n";
    }

    friend istream& operator>>(istream &in, SU &k)
    {
        in >> (Statie&) k;
        in >> k.legitimatii;
        in >> k.obiectiv;
    }

};

class SE : public Statie
{
    string obiectiv;

public:

    SE (string nume = "a", string strada = "b", int numar = -1, int sector = -1, vector<int> lista = {}, string obiectiv = "")
    : Statie (nume, strada, numar, sector, lista)
    {
        this->obiectiv = obiectiv;
    }

    void operator= (SE k)
    {
        nume = k.nume;
        strada = k.strada;
        numar = k.numar;
        sector = k.sector;
        lista = k.lista;
        obiectiv = k.obiectiv;
    }

    void afis()
    {
        afisare_statie();
        cout << "\n";
        if (obiectiv == "")
            cout << "Nu are obiective turistice in apropiere." << "\n";
        else
            cout << "Obiectiv turistic: " << obiectiv << "\n";
    }

    friend istream& operator>>(istream &in, SE &k)
    {
        in >> (Statie&) k;
        in >> k.obiectiv;
    }

};

template <typename T, typename Q>
class Pret : public Statie
{

    int pret = 2;
    char nume_statia1[15], nume_statia2[15];

    string ns1, ns2;
    void nume1()
    {
        strcpy(nume_statia1, typeid(T).name());
        while (nume_statia1[0] >= '0' && nume_statia1[0] <= '9')
            strcpy(nume_statia1, nume_statia1 + 1);
        ns1 = nume_statia1;
    }

    void nume2()
    {
        strcpy(nume_statia2, typeid(Q).name());
        while (nume_statia2[0] >= '0' && nume_statia2[0] <= '9')
            strcpy(nume_statia2, nume_statia2 + 1);
        ns2 = nume_statia2;
    }

public:
    int calatorie(T s1, Q s2)
    {
        nume1();nume2();
        cout << "Pretul calatoriei intre statia de tip " << ns1 <<", " << s1.nume << " si statia de tip " << ns2 << ", " << s2.nume << " este: ";
        if (ns1 == ns2 && ns1 == "SU")
        {
            int ok = 0;
            for (auto i : s1.lista)
                if (find (s2.lista.begin(), s2.lista.end(), i) != s2.lista.end())
                {
                    ok = 1;
                }
            if (ok == 1)
                return pret + pret * 0.15;
            else
                return pret;
        }
        else if (ns1 == ns2 && ns1 == "SE")
        {
            int ok = 0;
            for (auto i : s1.lista)
                if (find (s2.lista.begin(), s2.lista.end(), i) != s2.lista.end())
                {
                    ok = 1;
                }
            if (ok == 0)
                return pret + pret * 0.2;
            else
                return pret + pret * 0.25;
        }
        else if (ns1 != ns2)
        {
            int ok = 0;
            for (auto i : s1.lista)
                if (find (s2.lista.begin(), s2.lista.end(), i) != s2.lista.end())
                {
                    ok = 1;
                }
            if (ok == 0)
                return pret + pret * 0.3;
            else
                return pret + pret * 0.4;
        }

    }

};

template<typename T>
class Autobuz : public Statie
{
public:
    vector<T> autobuze;

    void adaugare(T k)
    {
        autobuze.push_back(k);
    }
/*
    void trece(int x)
    {
        vector<int>::iterator it;
        for (it = autobuze.begin(); it != autobuze.end(); it++)
        {
            if (find((*it).statii.begin(), (*it).statii.end(), x) != (*it).statii.end())
                cout << (*it).nume << " ";
        }
    }
*/
};

int main()
{
    SU a("Izvor", "SgMaj", 123, 6, {601, 336}, "Palatul"), b("ggg", "ddd", 22, 2, {601, 222}, "Da");
    SE c;

    Autobuz<SU> k;

    cout << a;

    Pret<SE, SE> sese;
    Pret<SU, SU> susu;
    Pret<SU, SE> suse;

    cout << susu.calatorie(a, b);

    k.adaugare(a);


    return 0;
}
