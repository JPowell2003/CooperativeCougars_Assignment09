# File Name : sales.py
# Student Name: Shantele King, Jay Powell, and Michael Slivinski
# email: king4sl@mail.uc.edu, powela9@mail.uc.edu, and slivinmb@mail.uc.edu
# Assignment Number: Assignment 09  
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work in a team to devlop a python project that extracts data from the Grocery Store Simulatro database using SQL. 

# Brief Description of what this module does. This module queries the database for the quantity of sales from the random product selected in the Product class in product.py.
# Citations: 
# https://stackoverflow.com/questions/53892462/how-to-get-rid-of-spaces-between-variables-and-strings-when-printed
# https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://dnmtechs.com/output-pyodbc-cursor-results-as-python-dictionary/
# Anything else that's relevant:

from dbconnector_Package.dbconnector import *
from product_Package.product import *

class Sales:
    '''
    Quries the amount of sales for the product that was selected in product.py.
    '''
    def __init__(self, conn):
        '''
        stores the database connection.
        '''
        self.conn = conn

    def fetch_sold(self,product_id):
        '''
        Retreives the total quantity sold for the random product ID that was previously selected.
        @param product_id: Id of the product
        @return: total number of units sold for random product
        '''
        db_manager = dbconnector()
        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold "
            "FROM dbo.tTransactionDetail "
            "INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID "
            "WHERE dbo.tTransaction.TransactionTypeID = 1 AND dbo.tTransactionDetail.ProductID = ?",
            (product_id,)
        )
        if cursor:
            result = cursor.fetchone()
            return result[0] if result else None
        return None