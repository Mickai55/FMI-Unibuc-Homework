package com.company;

public class Main {

    public static void main(String[] args) {

        Car c1 = new Car();
        System.out.println("Locuri: " + c1.seats);
        System.out.println("Usi: " + c1.getDoors());

        Bus b1 = new Bus();
        System.out.println("Locuri: " + b1.seats);
        System.out.println("Usi: " + b1.getDoors());

        Car c2 =  new Bus();
        System.out.println("Locuri: " + c2.seats);
        System.out.println("Usi: " + c2.getDoors());

    }
}