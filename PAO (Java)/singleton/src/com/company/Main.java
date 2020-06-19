package com.company;

public class Main {

    public static void main(String[] args) {
        // instantiating Singleton class with variable x
        Singleton x = Singleton.Singleton();

        // instantiating Singleton class with variable y
        Singleton y = Singleton.Singleton();

        // instantiating Singleton class with variable z
        Singleton z = Singleton.Singleton();

        // changing variable of instance x
        x.text = (x.text).toUpperCase();

        System.out.println("String from x is    " + x.text);
        System.out.println("String from y is    " + y.text);
        System.out.println("String from z is    " + z.text);
        System.out.println("\n");

        // changing variable of instance z
        z.text = (z.text).toLowerCase();

        System.out.println("String from x is    " + x.text);
        System.out.println("String from y is    " + y.text);
        System.out.println("String from z is    " + z.text);


    }
}
