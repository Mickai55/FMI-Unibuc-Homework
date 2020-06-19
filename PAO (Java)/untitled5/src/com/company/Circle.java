package com.company;

public class Circle extends Shape {

    @Override
    public void draw() {
        System.out.println("Draw a circle");
    }

    @Override
    public void delete() {
        System.out.println("Delete a circle");
    }
}
