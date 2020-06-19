package com.company;
import java.util.*;
import java.util.Random;

class sortNo implements Comparator<Client>
{
    public int compare(Client a, Client b)
    {
        return a.no - b.no;
    }
}

class sortBalance implements Comparator<Client>
{
    public int compare(Client a, Client b)
    {
        double k = a.getBalance() - b.getBalance();
        if (k < 0)
            return -1;
        else if (k > 0)
            return 1;
        return 0;
    }
}

class sortName implements Comparator<Client>
{
    public int compare(Client a, Client b)
    {
        if (a.getPerson().getLastName().compareTo(b.getPerson().getLastName()) != 0)
            return (a.getPerson().getLastName().compareTo(b.getPerson().getLastName()));
        else
            return (a.getPerson().getFirstName().compareTo(b.getPerson().getFirstName()));
    }
}

public class Bank {

    private String name;
    private int balance; // lei, euro????
    static int numberOfClients = 0;//private?
    public List<Client> clients = new ArrayList<Client>(); // private!!

    public Bank() { }

    public Bank(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }

    public int getBankBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }

    public String getName() {
        return name;
    }

    public void displayClients() {
        System.out.println("List with the bank '" + name + "' clients:");
        for (int i = 0; i < clients.size(); i++){
            System.out.println(clients.get(i));
        }
        System.out.println();
    }

    public void sortClientsByBalance(){
        Collections.sort(clients, new sortBalance());
    }

    public void sortClientsDefault(){
        Collections.sort(clients, new sortNo());
    }

    public void sortClientsByName(){
        Collections.sort(clients, new sortName());
    }

    public void addClient(Client x){
        clients.add(x);
    }

//    public <T> void addClientPremium(T x){
//        clients.add((Client) x);
//    } // ????

    public void removeClientByNo(int x){ clients.remove(x); }

    public void removeClientByCode(String x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client a = (Client) clients.get(i);
            if (a.cardCode == x) {
                clients.remove(i);
                break;
            }

        }
    }

    public <T> void convertToPremium(T x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client k = (Client) x;
            if (clients.get(i).cardCode == k.cardCode){
                Premium n = new Premium((Client) x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public <T> void convertToCredit(T x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client k = (Client) x;
            if (clients.get(i).cardCode == k.cardCode){
                Credit n = new Credit((Client) x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public <T> void convertToSavings(T x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client k = (Client) x;
            if (clients.get(i).cardCode == k.cardCode){
                Savings n = new Savings((Client) x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public <T> void convertToRevolving(T x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client k = (Client) x;
            if (clients.get(i).cardCode == k.cardCode){
                Revolving n = new Revolving((Client) x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public <T> void convertToInstallment(T x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client k = (Client) x;
            if (clients.get(i).cardCode == k.cardCode){
                Installment n = new Installment((Client) x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public int ClientLogin(String code, String pin){
        for(int i = 0; i < clients.size(); i++){
            if (clients.get(i).cardCode.equals(code))
                if (clients.get(i).PIN.equals(pin))
                    return i;
                else
                    return -1;
        }
        return -2;
    }

    public int findClient(String code) {
        for (int i = 0; i < clients.size(); i++)
            if (clients.get(i).cardCode.equals(code))
                return i;

        return -1;
    }

    public String generateCode(){
        // should be unique
        String a = new String();
        Random rand = new Random();
        for(int i = 0; i < 8; i++)
            a = a + String.valueOf(rand.nextInt(10));
        return a;
    }
}
