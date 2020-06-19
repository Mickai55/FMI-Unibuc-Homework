package com.company;
import java.util.*;

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
    }

    public void sortClientsByBalance(){
        Collections.sort(clients, new sortBalance());
    }

    public void sortClientsByName(){
        Collections.sort(clients, new sortName());
    }

    public void addClient(Client x){
        clients.add(x);
    }

    public <T> void addClientPremium(T x){
        clients.add((Client) x);
    } // ????

    public void removeClientByNo(int x){ clients.remove(x); }

    public void removeClientByLastName(String x){
        for (int i = 0; i < clients.size(); i++)
        {
            Client a = (Client) clients.get(i);
            if (a.getPerson().getLastName() == x) {
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
                Premium n = new Premium(k);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public void convertToCredit(Client x){
        for (int i = 0; i < clients.size(); i++)
        {
            if (clients.get(i).cardCode == x.cardCode){
                Credit n = new Credit(x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public void convertToSavings(Client x){
        for (int i = 0; i < clients.size(); i++)
        {
            if (clients.get(i).cardCode == x.cardCode){
                Savings n = new Savings(x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public void convertToRevolving(Client x){
        for (int i = 0; i < clients.size(); i++)
        {
            if (clients.get(i).cardCode == x.cardCode){
                Revolving n = new Revolving(x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }

    public void convertToInstallment(Client x){
        for (int i = 0; i < clients.size(); i++)
        {
            if (clients.get(i).cardCode == x.cardCode){
                Installment n = new Installment(x);
                clients.remove(i);
                clients.add(i, n);
            }
        }
    }
}
