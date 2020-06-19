package com.company;

public class Revolving extends Client {

    public Revolving() { }

    public Revolving(Client x){
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
                "} (Revolving)";
    }

    @Override
    public void loan(int sum, Bank bank){
        balance += sum;
        bank.setBalance(bank.getBankBalance() - sum);

        System.out.print("(" + this.name() + ") ");
        System.out.println("You have received " + sum + ". You are in debt " + sum * 1.05 + " (5% commission) to the bank " + bank.getName() + ".");
    }
}
