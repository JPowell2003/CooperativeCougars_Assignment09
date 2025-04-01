# dbconnector
import pyodbc


class dbconnector:
     def connect_to_database(self):
        '''
        connect to out SQL Server instance 
        @return the connection object
        '''

        try:
            conn = pyodbc.connect('Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=IS4010;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
        except:

           # print("Unable to connet to datebase") # Probably not wise 
            return None
        return conn

     def submit_sql_to_server(self, conn, sql_statement):
        '''
        Submit a SQL statement to our SQL Server
        @param conn: Connection object to the database
        @param sql_statement: The SQL query to execute
        @return: The pyodbc cursor object that contains the query results
        '''
        cursor = conn.cursor()
        cursor.execute(sql_statement)  # Now it actually uses the passed query!
        return cursor