package com.company;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseManage {

    private static final String DB_URL = "jdbc:mysql://127.0.0.1:3306/banca";
    private static final String USER = "root";
    private static final String PASSWORD = "1234567890";

    public void setUp() throws SQLException {
        String createTableSql = "CREATE TABLE IF NOT EXISTS persons (id int PRIMARY KEY AUTO_INCREMENT, name varchar(30)," + "age double)";

        Connection databaseConnection = DriverManager.getConnection(DB_URL, USER, PASSWORD);


    }


}

