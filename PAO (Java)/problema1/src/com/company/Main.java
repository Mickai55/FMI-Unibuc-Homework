package com.company;

public class Main {

    public static void main(String[] args) {
//        Person a = new Person("mihai", "cristian", 20, "1", "Student");
//        System.out.println(a);

        Person p = new Person();
        p.setName("ionel");
        p.setAge(100);
        p.setSurname("georgel");
        p.setType("Restant");
        p.setIdNo("1");

        Person k = new Person("mikai", "voika", 2, "da", "nu");

        System.out.println(p);

        Room r1 = new Room(1, "nice", 3);
        System.out.println(r1);

        Subject da = new Subject(r1, k, 3);
        System.out.println(da);

    }
}
