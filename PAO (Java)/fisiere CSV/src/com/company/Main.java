package com.company;

import javax.swing.*;
import java.io.*;
import java.util.Scanner;

public class Main {

    static int a = -1;

    public static void main(String[] args) {
        String text = "Voica,Mihai,20,Slatina";
        String filePath = "info.csv";

//        writeFile(text, filePath);

//        readFile(filePath);
        replace(filePath);

    }

    public static void writeFile(String text, String filePath) {
        try {
            FileWriter fw = new FileWriter(filePath, true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);

            pw.println(text);
            pw.flush();
            pw.close();

//            JOptionPane.showMessageDialog(null, "Success");
        }
        catch(Exception E){
            JOptionPane.showMessageDialog(null, "not Success");
        }

    }

    public static void readFile(String filePath){
        File file = new File(filePath);
        try {
            Scanner inputStream = new Scanner(file);
            while (inputStream.hasNext()){
                String line = inputStream.next();
                String[] words = line.split(",");
                System.out.println("Elev " + a++ + ":");
                System.out.println("Nume: " + words[0]);
                System.out.println("Prenume: " + words[1]);
                System.out.println("Varsta: " + words[2]);
                System.out.println("Oras: " + words[3]);
            }
            inputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void replace(String filePath){
        File file = new File(filePath);
        File tempFile = new File("myTempFile.csv");

        try {
            Scanner inputStream = new Scanner(file);
            while (inputStream.hasNext()) {
                String line = inputStream.next();
                String[] words = line.split(",");
                System.out.println(words[0]);
                if (words[0].equals("Coita")) {
                    String newLine = words[0] + "," + words[1] + "," + "692," + words[3];
                    writeFile(newLine, "myTempFile.csv");
                }
                else {
                    writeFile(line, "myTempFile.csv");
                }
            }
            inputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        file.delete();
        tempFile.renameTo(file);
    }
}
