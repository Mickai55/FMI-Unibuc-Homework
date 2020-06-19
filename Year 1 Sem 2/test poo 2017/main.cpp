#include <iostream>
#include <vector>
using namespace std;

class Student
{
public:
    string nume;
    string serie;
    int numar;
    double medie_bac;
    double medie_admitere;

    static int nr;

public:

    Student(string nume = "da", string serie = "da", int numar = -1, double medie_bac = -1)
    {
        this->nume = nume;
        this->serie = serie;
        this->numar = numar;
        this->medie_bac = medie_bac;
        nr++;
    }

    friend istream& operator>>(istream &in, Student &k)
    {
        in >> k.nume >> k.serie >> k.numar >> k.medie_bac;
        return in;
    }

    void afisare_student()
    {
        cout << nume << " " << serie << " "<< numar << " "<< medie_bac << " ";
    }

    virtual void afis()
    {
        afisare_student();
    }

    friend ostream& operator<<(ostream &out, Student &k)
    {
        k.afis();
        out << "\n";
        return out;
    }
};

int Student::nr = 0;

class StudentID : public Student
{
    double nota_mate;

public:
    StudentID (string nume = "da", string serie = "da", int numar = -1, double medie_bac = -1, double nota_mate = -1) :
               Student(nume, serie, numar, medie_bac)
    {
        this->nota_mate = nota_mate;
    }

    void afis()
    {
        afisare_student();
        cout << " " << nota_mate;
    }

    friend ostream& operator<<(ostream &out, StudentID &k)
    {
        k.afis();
        return out;
    }

};

class Student2 : public Student
{
    double medie_absolvire;
    string program;

public:
    Student2 (string nume = "da", string serie = "da", int numar = -1, double medie_bac = -1, double medie_absolvire = -1, string program = "da") :
               Student(nume, serie, numar, medie_bac)
    {
        this->medie_absolvire = medie_absolvire;
        this->program = program;
    }

    void afis()
    {
        afisare_student();
        cout << " " << medie_absolvire << " " << program << "\n";
    }

    friend ostream& operator<<(ostream &out, Student2 &k)
    {
        k.afis();
        return out;
    }
};

template<typename T>
class Inscriere : public Student
{
public:
    vector<T> studenti;
    static int numar;

    void inscriere(T k)
    {
        studenti.push_back(k);
        numar++;
    }

    void afisare_studenti()
    {
        int u = 0;
        typename vector<T>::iterator it;
        for (it = studenti.begin(); it != studenti.end(); it++)
        {
            u++;
            cout << "STUDENTUL " << u << ":\n";
            cout << *it << "\n";
        }
    }

    void stergere_student(T k)
    {
        typename vector<T>::iterator it;
        for (it = studenti.begin(); it != studenti.end(); it++)
            if (k.nume == (*it).nume)
                studenti.erase(it);
    }

    void examen_IF(Student &k)
    {
        int nota_proba_scrisa;
        cout << "Studentul " << k.nume << " a primit nota urmatoare la scris: ";
        cin >> nota_proba_scrisa;
        k.medie_admitere = 0.8 * nota_proba_scrisa + 0.2 * k.medie_bac;
    }

    void examen_ID(StudentID &k)
    {
        int nota_proba_orala;
        cout << "Studentul a primit nota urmatoare la oral: ";
        cin >> nota_proba_orala;
        k.medie_admitere = 0.6 * nota_proba_orala + 0.4 * k.medie_bac;
    }

    void examen_fac2(Student2 &k)
    {
        int nota_proba_orala;
        cout << "Studentul a primit nota urmatoare la oral: ";
        cin >> nota_proba_orala;
        k.medie_admitere = 0.6 * nota_proba_orala + 0.4 * k.medie_absolvire;
    }

    void studenti_admisi()
    {
        typename vector<T>::iterator it;

        for (it = studenti.begin(); it != studenti.end(); it++)
        {
            examen_IF((*it));
        }

        for (it = studenti.begin(); it != studenti.end(); it++)
        {
            cout << "Studentul: ";
            cout << (*it).nume;
            if ((*it).medie_admitere >= 5)
                cout << " a fost admis cu media " << (*it).medie_admitere << "\n";
            else
                cout << " a fost respins cu media " << (*it).medie_admitere << "\n";

        }
        cout << "\n";

    }

};

template <typename T> int Inscriere<T>::numar = 0;

int main()
{
    Student a, b("dadadada", "OT", 1234, 6.01), c("viorel", "B", 555555, 9.50);
    Inscriere<Student> iff;
    int x, y;
    iff.inscriere(a); iff.inscriere(b); iff.inscriere(c);

    Student2 aa, bb("dadadada", "OT", 1234, 6.01, 5, "calll");
    Inscriere<Student2> id;
    id.inscriere(aa); id.inscriere(bb);
    id.afisare_studenti();

    cout << Inscriere<Student2>::numar;




  /*  do
    {
        cout << "Alegeti un numar: \n";
        cout << "1. Introduceti un student nou. \n";
        cout << "2. Afisati lista cu studentii. \n";
        cout << "3. Afisati lista cu studentii admisi. \n";
        cout << "0. Iesire. \n";
        cout << "Alege:(1/2/3/0)"; cin >> x;
        if (x == 1)
        {
            cout << "Alegeti un numar: \n";
            cout << "1. La IF. \n";
            cout << "2. La ID. \n";
            cout << "3. La a doua facultate. \n";
            cout << "Alege:(1/2/3)"; cin >> y;
            if (y == 1)
            {
                Student p;
                cin >> p;
                id.inscriere(p);
            }
            else if (y == 2)
            {
                StudentID p;
                cin >> p;
                id.inscriere(p);
            }
            else if (y == 3)
            {
                Student2 p;
                cin >> p;
                id.inscriere(p);
            }
        }
        else if (x == 2)
        {
            id.afisare_studenti();
        }
        else if (x == 3)
        {
            id.studenti_admisi();
        }

    } while (x != 0);
*/

    return 0;
}
