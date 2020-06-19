package com.company;

public class Main {

    public static void main(String[] args) {
        SetUpData setUpData = new SetUpData();
        PersonRepository personRepository = new PersonRepository();

        setUpData.setUp();
//        personRepository.insertPerson(new Person(10, "Mihai", 20)); NU MERGE
//        setUpData.addPerson("Costel","Ion","Male","22221111","1235" ,"133.0","Lei",0,"Premium");


//        personRepository.updatePersonBalance("1234", "17265633");
//        personRepository.deletePerson("22221111");
//
        String person = personRepository.getPersonByCode("17265633");
        System.out.println(person);

//        setUpData.displayPersons();
    }
}
