package com.company;

public class HelloThread extends Thread {

    // main method of a thread
    @Override
    public void run(){
        for (int i = 0; i <= 10; i++)
            System.out.println("Hello from another!");
    }
}