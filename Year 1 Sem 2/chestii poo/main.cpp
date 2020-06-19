#include<iostream>
using namespace std;

class loc{
    int longitude, latitude;
public:
    loc(){
        longitude = 0; latitude = 0;
    };
    loc(int lg, int lt) { longitude = lg; latitude = lt; }
    void show() {
        cout << longitude << " ";
        cout << latitude << "\n";
    }
    loc operator+(loc op2);
    loc operator-(loc op2);
    loc operator=(loc op2);
    loc operator++();
    friend ostream &operator<<(ostream &out, const loc &a);
    friend istream &operator>>(istream &in, loc &a);
};

loc loc::operator+(loc op2){
    loc temp;
    temp.longitude = op2.longitude + longitude;
    temp.latitude = op2.latitude + latitude;
    return temp;
}

loc loc::operator-(loc op2){
    loc temp;
    temp.longitude = longitude - op2.longitude;
    temp.latitude = latitude - op2.latitude;
    return temp;
}

loc loc::operator=(loc op2){
    longitude = op2.longitude;
    latitude = op2.latitude;
    return *this;
}

loc loc::operator++(){
    this->longitude++;longitude++;(*this).longitude++;
    this->latitude++;

}

ostream &operator<< (ostream &out, const loc &a)
{
    out << a.longitude << " " << a.latitude << endl;
    return out;
}

istream &operator>>(istream &in, loc &a)
{
    in >> a.longitude;
    in >> a.latitude;
    return in;
}

int main()
{
    loc x(1, 2), y (2, 5), z;
    cin >> y;
    cout << y;

    return 0;
}
