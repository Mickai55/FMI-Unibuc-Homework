package com.company;

public class Class1 {

    @Override
    public String toString() {
        return "Class1{" +
                "nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                '}';
    }

    String nume;

    public Class1(String nume, String prenume) {
        this.nume = nume;
        this.prenume = prenume;
    }

    String prenume;
}
