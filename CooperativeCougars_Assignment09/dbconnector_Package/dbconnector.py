
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