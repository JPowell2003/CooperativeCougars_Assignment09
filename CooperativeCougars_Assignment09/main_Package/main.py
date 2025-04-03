# File Name : main.py
# Student Name: Shantele King, Jay Powell, and Michael Slivinski
# email: king4sl@mail.uc.edu, powela9@mail.uc.edu, and slivinmb@mail.uc.edu
# Assignment Number: Assignment 09  
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work in a team to devlop a python project that extracts data from the Grocery Store Simulatro database using SQL. 

# Brief Description of what this module does. This module retrieves the manufacturer name, brand name, sales name, and product description from classes in other packages 
#                                             to create a sentence describing a random product and its sales. 
# Citations: 
# https://stackoverflow.com/questions/53892462/how-to-get-rid-of-spaces-between-variables-and-strings-when-printed
# https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
# https://dnmtechs.com/output-pyodbc-cursor-results-as-python-dictionary/
# Anything else that's relevant:


from dbconnector_Package.dbconnector import *
from product_Package.product import *
from sales_Package.sales import *

import pyodbc


if __name__ == "__main__":

    db_manager = dbconnector()
    conn = db_manager.connect_to_database()
    
 
    product_manager = Product(conn)
    random_product = product_manager.fetch_random_product()

   
    manufacturer_name = product_manager.fetch_manufacturer(random_product["ManufacturerID"])


    brand_name = product_manager.fetch_brand(random_product["BrandID"])


    sales_manager = Sales(conn)
    sales_quantity = sales_manager.fetch_sold(random_product["ProductID"])

    product_description = random_product["Description"]
    print(f"{brand_name} has the product {product_description or 'unknown'}, which is manufactured by {manufacturer_name} and has {sales_quantity} of total sales." )

   

 