package com.company;
import java.util.Scanner;

public class Management{

    public void manage() {

        Bank bank1 = new Bank("BRD", 999999);

        Person p;

        Revolving c1 = new Revolving(p = new Person("Costel", "Ion", "Male"), "22222222", "1235", 10000, "Lei", bank1);
        Client c2 = new Client(p = new Person("Voica", "Mihai", "Male"), "11111111", "1234", 10, "Lei", bank1);
        Premium c3 = new Premium(p = new Person("Ionescu", "Andrei", "Male"), "33333333", "1223", 200, "Lei", bank1);

        Login(bank1);

    }

    public void Login(Bank bank)
    {
        Scanner scan = new Scanner(System.in);
        int sw = 0;
        while (sw <= 3) {
            System.out.println("Choose:");
            System.out.println("1 -> Login.");
            System.out.println("2 -> Create a new account.");
            System.out.println("3 -> See clients.");
            System.out.println("4 -> Exit.");
            System.out.print("Choice ->");
            sw = scan.nextInt();

            //Login
            if (sw == 1) {
                scan = new Scanner(System.in);
                System.out.print("Card Code:");
                String cc = scan.nextLine();
                System.out.print("PIN:");
                String pin = scan.nextLine();

                int r = bank.ClientLogin(cc, pin);
                if (r == -1)
                    System.out.println("Wrong PIN.");
                else if (r == -2)
                    System.out.println("Client not found.");
                else
                    {
                    int sw2 = 0;
                    System.out.println("\nLogin succesful!");
                    System.out.println("Welcome " + bank.clients.get(r).name() + "!");
                    while(sw2 <= 6)
                    {
                        System.out.println("Choose:");
                        System.out.println("1 -> Display balance.");
                        System.out.println("2 -> Withdraw.");
                        System.out.println("3 -> Add balance.");
                        System.out.println("4 -> Make a loan.");
                        System.out.println("5 -> Send money.");
                        System.out.println("6 -> Delete account.");

                        //............
                        System.out.println("7 -> Log Out.");
                        System.out.print("Choice ->");
                        sw2 = scan.nextInt();

                        // Display balance
                        if (sw2 == 1){
                            bank.clients.get(r).displayBalance();
                        }

                        // Withdraw
                        else if (sw2 == 2){
                            System.out.println("Sum to withdraw: ");
                            int s = scan.nextInt();
                            bank.clients.get(r).withdraw(s);
                        }

                        // Add balance
                        else if (sw2 == 3){
                            System.out.println("Sum to add: ");
                            int s = scan.nextInt();
                            bank.clients.get(r).addBalance(s);
                        }

                        // Loan
                        else if (sw2 == 4){
                            System.out.println("Sum to loan: ");
                            int s = scan.nextInt();
                            bank.clients.get(r).loan(s, bank);
                        }

                        // Send Money
                        else if (sw2 == 5){
                            System.out.println("Enter the Card Code of the person you want to send money to:");
                            scan = new Scanner(System.in);
                            String s = scan.nextLine();
                            int n = bank.findClient(s);
                            if (n == -1)
                                System.out.println("Client not found!");
                            else {
                                System.out.println("Sum to send: ");
                                int S = scan.nextInt();
                                bank.clients.get(r).sendMoney(bank.clients.get(n), S);

                                System.out.println("Success!");
                            }

                        }

                        // Delete account
                        else if (sw2 == 6){
                            scan = new Scanner(System.in);
                            System.out.println("Are you sure? (y/n)");
                            String s = scan.nextLine();
                            if (s.equals("y")) {
                                bank.removeClientByNo(r);
                                System.out.println(bank.clients.get(r).name() + " deleted!");
                                break;
                            }
                        }
                    }
                }
            }

            //Create a new account
            else if (sw == 2){
                scan = new Scanner(System.in);
                System.out.print("Last Name:");
                String lastName = scan.nextLine();
                System.out.print("First Name:");
                String firstName = scan.nextLine();
                System.out.print("Sex:");
                String sex = scan.nextLine();
                String cardCode = bank.generateCode();
                System.out.print("Pin:");
                String pin = scan.nextLine();
                Person p = new Person(firstName, lastName, sex);

                
                Client c = new Client(p, cardCode, pin, 0, "Lei", bank);

                System.out.println("Hello, " + firstName + " " + lastName + "! " + "Your unique card code is: " + cardCode + ".");
                System.out.println("Now you can login!");
            }

            //Bank clients
            else if (sw == 3){
                manageClients(bank);
            }
        }
    }


    public void manageClients(Bank bank)
    {
        Scanner scan = new Scanner(System.in);
        int sw = 0;
        while (sw <= 3) {
            System.out.println("Choose:");
            System.out.println("1 -> Display all clients.");
            System.out.println("2 -> Display all clients sorted by name.");
            System.out.println("3 -> Display all clients sorted by balance.");
            System.out.println("4 -> Back.");
            System.out.print("Choice ->");
            sw = scan.nextInt();

            if (sw == 1) {
                bank.displayClients();
            } else if (sw == 2) {
                bank.sortClientsByName();
                bank.displayClients();
                bank.sortClientsDefault();
            } else if (sw == 3) {
                bank.sortClientsByBalance();
                bank.displayClients();
                bank.sortClientsDefault();
            }
        }
    }
}
