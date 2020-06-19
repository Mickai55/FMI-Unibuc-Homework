#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string sdf[]={"bug","kg" };
class Produs
{
public:
    string nume;
    double pret;
    int cantitate;
    int zi;
    int luna;
    int an;
    int discount;

public:
    Produs(string nume = "nu", double pret = -1, int cantitate = -1, int zi = -1, int luna = -1, int an = -1, int discount = 0)
    {
        this->nume = nume;
        this->pret = pret;
        this->cantitate = cantitate;
        this->zi = zi;
        this->luna = luna;
        this->an = an;
        this->discount = discount;
    }

    friend istream& operator>>(istream &in, Produs &k)
    {
        in >> k.nume >> k.pret >> k.cantitate >> k.zi >> k.luna >> k.an;
        return in;
    }

    void afisare_produs()
    {
        cout << "Data adaugarii: " << zi << " " << luna << " " << an << "\n";
        cout << "Nume: " << nume << "\n";
        cout << "Pret: " << pret << " lei/buc\n";
        cout << "Cantitate: " << cantitate << "\n";
        if (discount != 0)
            cout << "Discount: " << discount << "%\n";
    }

    virtual void afis()
    {
        afisare_produs();
        cout << "\n";
    }

    friend ostream& operator<<(ostream &out, Produs &k)
    {
        k.afis();
        return out;
    }

};

class Perisabil : public Produs
{
    int valabilitate;

public:

    Perisabil(string nume = "nu", double pret = -1, int cantitate = -1, int zi = -1, int luna = -1, int an = -1, int valabilitate = -1) : Produs(nume, pret, cantitate, zi, luna, an)
    {
        this->valabilitate = valabilitate;
    }

    friend istream& operator>>(istream &in, Perisabil &k)
    {
        in >> (Produs&) k;
        in >> k.valabilitate;
        return in;
    }

    void afis()
    {
        afisare_produs();
        cout << "Cantitate: " << cantitate << " kg\n";
        cout << "Valabilitate: " << valabilitate << " zile\n";
    }
};

class Bautura : public Produs
{
public:
    Bautura(string nume = "nu", double pret = -1, int cantitate = -1, int zi = -1, int luna = -1, int an = -1) : Produs(nume, pret, cantitate, zi, luna, an)
    {}

    void afis()
    {
        afisare_produs();
        cout << "Cantitate: " << cantitate << " l\n";
    }

};

class Obiect : public Produs
{
    Obiect(string nume = "nu", double pret = -1, int cantitate = -1, int zi = -1, int luna = -1, int an = -1) : Produs(nume, pret, cantitate, zi, luna, an)
    {}

    void afis()
    {
        afisare_produs();
        cout << "Cantitate: " << cantitate << " bucati\n";
    }

};

class Vanzare : public Produs
{

public:vector<Produs> stoc;
    void adaugare_stoc(Produs k)
    {
        stoc.push_back(k);
    }

    void afisare_stoc()
    {
        cout << "STOC:\n\n";
        vector<Produs>::iterator it;
        for (it = stoc.begin(); it != stoc.end(); it++)
            cout << *it;
    }

    void scoatere_stoc(Produs k)
    {
        vector<Produs>::iterator it;
        for (it = stoc.begin(); it != stoc.end(); it++)
            if ((*it).nume == k.nume)
            {
                stoc.erase(it);
                break;
            }
    }

    void vanzare(string k, int cant)
    {
        vector<Produs>::iterator it = stoc.begin();
        int aux = cant;
        while (it != stoc.end())
        {
            if ((*it).nume == k)
            {
                if ((*it).cantitate < cant)
                {
                    cant = cant - (*it).cantitate;
                    scoatere_stoc((*it));
                    it = stoc.begin();
                }
                else
                {
                    (*it).cantitate = (*it).cantitate - cant;
                    cout << "A fost vandut produsul: " << k;
                    cout << "\nCantitate: " << cant;
                    cout << "\nIncasari: " <<((*it).pret - (*it).discount * (*it).pret / 100) * cant << " lei\n";
                    break;
                }
            }
            else
                it++;
            if (it == stoc.end() && cant != 0)
                cout << "Nu mai exista " << k << " in stoc.\n\n";
        }
    }

    void verificare_data (int z1, int l1, int a1, int z2, int l2, int a2)
    {
        vector<Produs>::iterator it;
        for (it = stoc.begin(); it != stoc.end(); it++)
        {
            if (a1 < (*it).an && (*it).an < a2)
            {
                cout << (*it);
                continue;
            }
            else if (a1 == a2 && a2 == (*it).an)
                if (l1 < (*it).luna && (*it).luna < l2)
                {
                    cout << (*it);
                    continue;
                }
                else if (l1 == l2 && l2 == (*it).luna)
                    if ((z1 < (*it).zi && (*it).zi < z2) || z1 == z2 == (*it).zi)
                    {
                        cout << (*it);
                        continue;
                    }
        }
    }

};



int main()
{
    Produs a("pule", 2, 100, 12, 12, 2010, 20), b("pule", 3, 100, 11, 9, 1999), c("caca", 10, 120, 15, 12, 2010);
    Vanzare v;
    v.adaugare_stoc(a);v.adaugare_stoc(b);v.adaugare_stoc(c);
    v.afisare_stoc();
    v.vanzare("pule", 222);

    return 0;
}
