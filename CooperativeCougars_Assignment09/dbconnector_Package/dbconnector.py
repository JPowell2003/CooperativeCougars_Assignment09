# File Name : main.py
# Student Name: Shantele King, Jay Powell, and Michael Slivinski
# email: king4sl@mail.uc.edu, powela9@mail.uc.edu, and slivinmb@mail.uc.edu
# Assignment Number: Assignment 09  
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work in a team to devlop a python project that extracts data from the Grocery Store Simulatro database using SQL. 

# Brief Description of what this module does. This module connects our SQL server and and allows us to input SQL statements to the server 
# Citations: 
# https://stackoverflow.com/questions/53892462/how-to-get-rid-of-spaces-between-variables-and-strings-when-printed
# https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://dnmtechs.com/output-pyodbc-cursor-results-as-python-dictionary/
# Anything else that's relevant:
# dbconnector
import pyodbc


class dbconnector:
     def connect_to_database(self):
        '''
        connect to our SQL Server instance 
        @return the connection object
        '''
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                'Database=GroceryStoreSimulator;'
                                'uid=IS4010Login;'
                                'pwd=P@ssword2;')
        except:   
            return None
        return conn

     def submit_sql_to_server(self, conn):
        '''
        Submit a SQL statement to our SQL Server
        @param conn: Connection object to the database
        @param sql_statement: The SQL query to execute
        @return: The pyodbc cursor object that contains the query results
        '''
        cursor = conn.cursor()
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        
        cursor.execute(query)
        return cursor