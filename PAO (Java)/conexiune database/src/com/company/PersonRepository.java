package com.company;

import java.sql.*;

public class PersonRepository {

    // PreparedStatement
    public String getPersonByCode(String code) {
        String selectSql = "SELECT * FROM clients WHERE Card_code = ?";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(selectSql);
            preparedStatement.setString(1, code);

            ResultSet resultSet = preparedStatement.executeQuery();

            if (resultSet.next()){
                return (resultSet.getString(1) + ", " + resultSet.getString(2) + ", "  + resultSet.getString(3) +
                ", "  + resultSet.getString(4) + ", "  + resultSet.getString(5) + ", "  + resultSet.getString(6) +
                ", "  + resultSet.getString(7) + ", "  + resultSet.getString(8) + ", "  + resultSet.getString(9));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    // PreparedStatement
    public void updatePersonBalance(String Balance, String code) {
        String updateNameSql = "UPDATE clients SET Balance=? WHERE Card_code=?";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(updateNameSql);
            preparedStatement.setString(1, Balance);
            preparedStatement.setString(2, code);

            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deletePerson(String code) {
        String deleteSql = "DELETE FROM clients WHERE Card_code = ?";

        Connection databaseConnection = DatabaseConfiguration.getDatabaseConnection();
        try {
            PreparedStatement preparedStatement = databaseConnection.prepareStatement(deleteSql);
            preparedStatement.setString(1, code);

            preparedStatement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}