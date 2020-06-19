#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector <int> a = {1, 2, 3};
    vector<int> b(10, 2);

    for (auto i : a)
        cout << i << " ";

    vector<int> *it = find(a.begin(), a.end(), 2);
    cout << it;

    // a.push_back(3);
    // a.push_back(2);
    // a.push_back(1);
    // sort (a.begin(), a.end());
    // for (auto i:b)
    //     cout << i << " ";
    // cout << endl;
    // cout << *a.begin() << " " << *(a.end() - 1) << endl;
    // cout << a.front() << " " << a.back();


    return 0;
}
