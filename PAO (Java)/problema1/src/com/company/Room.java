package com.company;

class Room
{
    private int number;
    private String type;
    private int floor;

    public Room(){}

    public Room(int number, String type, int floor)
    {
        this.number = number;
        this.type = type;
        this.floor = floor;
    }

    public int getNumber()
    {
        return number;
    }

    public String getType()
    {
        return type;
    }

    public int getFloor()
    {
        return floor;
    }

    public void setNumber(int a)
    {
        number = a;
    }

    public void setType(String a)
    {
        type = a;
    }

    public void setFloor(int a)
    {
        floor = a;
    }

    @Override
    public String toString()
    {
        return "Room(" + number + " " + type + " " + floor + ");";
    }
}