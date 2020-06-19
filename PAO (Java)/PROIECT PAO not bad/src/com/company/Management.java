package com.company;

public class Management{

    public void manage() {

        Bank bank1 = new Bank("BRD", 999999);

        Person p;

        Client c1 = new Client(p = new Person("Costel", "Ion", "Male"), "222222", "1235", 10000, "Lei", bank1);
        Client c2 = new Client(p = new Person("Voica", "Mihai", "Male"), "111111", "1234", 10, "Lei", bank1);

        Premium c3 = new Premium(p = new Person("Ionescu", "Andrei", "Male"), "333333", "1223", 200, "Lei", bank1);

        bank1.convertToInstallment(c2);

        bank1.convertToPremium(c2); // converteste doar in vector!!!

        bank1.clients.get(1).withdraw(200);

//        c1.withdraw(540);
//        bank1.sortClientsByBalance();
//        bank1.sortClientsByName();
//        bank1.removeClientByNo(0);
//        bank1.removeClientByLastName("Popescu");
//        c1.sendMoney(c2, 100);
//        c2.loan(1000, bank1);
//        c1.addBalance(100);


        bank1.displayClients();
    }

}
