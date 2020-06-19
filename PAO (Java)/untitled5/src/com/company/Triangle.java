package com.company;

public class Triangle extends Shape {

    @Override
    public void draw() {
        System.out.println("Draw a triangle.");
    }

    @Override
    public void delete() {
        System.out.println("Delete the triangle");
    }
}
