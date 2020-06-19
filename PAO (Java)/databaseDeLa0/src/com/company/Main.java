package com.company;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {

    public static void main(String[] args) throws SQLException {
        DatabaseManage db = new DatabaseManage();
        db.setUp();

    }
}
