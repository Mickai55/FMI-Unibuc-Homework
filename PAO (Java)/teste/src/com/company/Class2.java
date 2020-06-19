package com.company;

public class Class2 extends Class1 {
    @Override
    public String toString() {
        return "Class2{" +
                "ani=" + ani +
                ", nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                '}';
    }

    public Class2(String nume, String prenume, int ani) {
        super(nume, prenume);
        this.ani = ani;
    }

    int ani;
}
