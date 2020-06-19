package com.company;

public class Savings extends Client {

    public Savings() { }

    public Savings(Person person, String cardCode, String PIN, int balance, String currency, Bank bank){
        super(person, cardCode, PIN, balance, currency, bank);
    }

    public Savings(Client x){
        this.person = x.getPerson();
        this.cardCode = x.cardCode;
        this.PIN = x.PIN;
        this.balance = x.balance;
        this.currency = x.currency;
        this.no = x.no;
        //bank??
    }

    @Override
    public String toString() {
        return "Client number " + no + " {" +
                "lastName = '" + this.getPerson().getLastName() + '\'' +
                ", firstName = '" + this.getPerson().getFirstName() + '\'' +
                ", balance = '" + this.getBalance() + '\'' + // stergere??
                "} (Savings)";
    }

    @Override
    public void addBalance(int x){

        this.balance += x * 1.25;

    }

}
