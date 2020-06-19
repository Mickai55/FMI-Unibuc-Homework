package com.company;

public class Installment extends Client {

    public Installment() { }

    public Installment(Client x){
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
                "} (Credit)";
    }

    @Override
    public void sendMoney(Client client, double sum) {
        if (this.getBalance() - sum >= 0) {
            this.setBalance(this.getBalance() - sum);
            client.setBalance(client.getBalance() + sum + 1.25 * sum);
        }
        else
            System.out.println("You don't have the requested sum disposable! (" + this.name() + ", " + sum + ").");
    }
}
