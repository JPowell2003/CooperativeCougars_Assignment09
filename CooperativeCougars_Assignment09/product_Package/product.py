# File Name : product.py
# Student Name: Shantele King, Jay Powell, and Michael Slivinski
# email: king4sl@mail.uc.edu, powela9@mail.uc.edu, and slivinmb@mail.uc.edu
# Assignment Number: Assignment 09  
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work in a team to devlop a python project that extracts data from the Grocery Store Simulatro database using SQL. 

# Brief Description of what this module does. This model gives us code to get both the manufacturer and brand name. It also grabs product data at random.
# Citations: 
# https://stackoverflow.com/questions/53892462/how-to-get-rid-of-spaces-between-variables-and-strings-when-printed
# https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://dnmtechs.com/output-pyodbc-cursor-results-as-python-dictionary/
# Anything else that's relevant:

import random
from dbconnector_Package.dbconnector import *

class Product:
    """
    Handles product selection and manufacturer/brand lookup.
    """

    def __init__(self, conn):
        self.conn = conn  # Stores the database connection for future queries

    def fetch_random_product(self):
        '''
        Get product data and select a random product
        @return: A dictionary containing the selected product's details
        '''
        db_manager = dbconnector()
        cursor = db_manager.submit_sql_to_server(self.conn)

        if cursor:  # Ensures that the database query actually returns a valid cursor
            products = cursor.fetchall()

            if products:  # Makes sure the query actually returned some data
                random_product = random.choice(products)
                return {
                    "ProductID": random_product[0],
                    "UPC_A": random_product[1],
                    "Description": random_product[2],
                    "ManufacturerID": random_product[3],
                    "BrandID": random_product[4]
                }
        return None  # Returns None if no data is available


    def fetch_manufacturer(self, manufacturer_id):
            '''
            Get manufacturer name using ManufacturerID
            @return: Manufacturer name
            '''
            db_manager = dbconnector()
            cursor = self.conn.cursor()
            cursor.execute( "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?", (manufacturer_id,))
            if cursor:
                result = cursor.fetchone()
                return result[0] if result else None
            return None

    def fetch_brand(self, brand_id):
            '''
            Get brand name using BrandID
            @return: Brand name
            '''
            db_manager = dbconnector()
            cursor = self.conn.cursor()
            cursor.execute( "SELECT Brand FROM tBrand WHERE BrandID = ?", (brand_id,))
            if cursor:
                result = cursor.fetchone()
                return result[0] if result else None
            return None




