#include "AFN.h"

#define MAX_STATE INT_MAX
#define MAX_SYMBOL INT_MAX

AFN::AFN () { }

AFD& AFN::turn_into_AFD ( )
{
    //Initializarea dimensiunii si alfabetului AFD-ului
    queue < set <int> > states_to_check; // Coada in care stocam starile/multimile de stari ale AFN-ului
    vector < set <int> > states; // Starile AFD-ului
    set < int > current_state; //Starea curenta pe care o verificam
    states.resize (0);
    current_state.insert (si);
    states_to_check.push (current_state);
    int numar_stari = 0;
    while (!states_to_check.empty ())
    {
        current_state = states_to_check.front ();
        states_to_check.pop ();
        int ok = 0;
        // Verificam daca starea nu a fost deja introdusa in AFD
        for (vector <set < int > >:: iterator i = states.begin (); i != states.end (); i++)
            if (*i == current_state)
            {
                ok = 1; break;
            }
        if (ok == 1) continue;
        for (int j = 0; j < na; j++)
        {
                set < int > s; // Starea in care duce litera curenta
                for (set<int>::iterator i = current_state.begin(); i != current_state.end (); i++ )
                {
                    if ( transition[*i][j].size () == 0)
                        continue;
                    for (set <int> :: iterator k = transition[*i][j].begin (); k!= transition [*i][j].end (); k++)
                        s.insert (*k);
                }
                if ( ! s.empty ())
                states_to_check.push (s);
        }
        numar_stari++;
        states.push_back (current_state);
    }


    AFD temp (numar_stari, na);
    strcpy ( temp.a, a);
    temp.transition.resize (temp.nq);
    for (int i = 0; i < temp.nq; i++)
    {
        temp.transition[i].resize (temp.na);
    }
    /*
      Avem un vector cu multimea de stari ale AFD-ului rezultat
      Pe baza acestuia von crea noua matrice pentru functiile de tranzitie
      Pentru fiecare stare/ multime de stari din vector atribuim un nou indice in AFD
    */
    for (int it = 0; it < temp.nq; it++ )
    {
        current_state = states[it];
        int stare_finala = 0;
        for (int j = 0; j < na; j++)
        {
                set < int > s;
                for (set<int>::iterator i = current_state.begin(); i != current_state.end (); i++ )
                {
                    if (f[*i] == true) stare_finala = 1;
                    if ( transition[*i][j].size () == 0)
                        continue;
                    for (set <int> :: iterator k = transition[*i][j].begin (); k!= transition [*i][j].end (); k++)
                          s.insert (*k);
                }
                // Cautam starea s obtinuta in vectorul de stari si o inseram in AFD
                if ( s.empty ())
                    temp.transition[it][j] = -1;
                else
                {
                    for (int k = 0; k < temp.nq; k++)
                    if ( s == states[k])
                    {
                        temp.transition[it][j] = k;
                        temp.nt ++;
                        break;
                    }
                }
        }
        temp.f[it] = stare_finala;
    }
    cout << temp;


}

std::istream& operator>>(std::istream& in, AFN& afn)
{
    in >> afn.nq;
    afn.vect = new int[afn.nq + 1];
    afn.f = new bool [10000];
    for (int i = 0; i < afn.nq; i++)
        in >> afn.vect[i];
    in >> afn.na;
    afn.transition.resize (10000);
    for (int i = 1; i < 10000; i++)
    {
        afn.f[i] = false;
        afn.transition[i].resize (afn.na + 1);
    }
    afn.a = new char [afn.na + 1];
    for (int i = 0; i < afn.na; i++)
        in >> afn.a[i];
    in >> afn.si;//starea initiala
    in >> afn.sf;//starile finale
    afn.SF = new int[afn.nq + 1];
    for (int i = 0; i < afn.sf; i++)
    {
        in >> afn.SF[i];
        afn.f[afn.SF[i]] = 1;
    }
    int q1, q2, poz;
    char c, *p;
    in >> afn.nt;// Numarul funtiilor de trazitie
    for (int i = 1; i <= afn.nt; i++)
    {
        in >> q1 >> c >> q2;
        p = strchr (afn.a , c);
        if (p == NULL)
        {
            cout << "Eroare la citire ! \n";
            exit(0);
        }
        poz = p - afn.a;
        afn.transition[q1][poz].insert (q2);
    }
    return in;
}

