# Product.py
# Sources:
# https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://dnmtechs.com/output-pyodbc-cursor-results-as-python-dictionary/

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
