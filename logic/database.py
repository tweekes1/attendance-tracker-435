from os import environ
from pymysql import connect, cursors, Error

# Database class that will be used to access the information for the application

class Database():
    def __init__(self):
        host = environ.get('MYSQL_HOST')
        user = environ.get('MYSQL_USER')
        password = environ.get('MYSQL_PASSWORD')
        db = environ.get('MYSQL_DB')

        # initializes the connection for the database
        self.db_con = connect(
            host = host,
            user = user,
            password = password,
            db = db,
            cursorclass = cursors.DictCursor
        )

        # initializes the cursor for the database
        # what runs queries
        self.cursor = self.db_con.cursor()

    # Inserts user into [USER_TABLE] based on the schema given in the readme
    def create_user(self, user_name, user_email, user_password, user_type):
        sql_query = 'INSERT INTO users (`name`, `email`, `password_hash`, `user_type`) VALUES (%s, %s, %s, %s)'

        try: 
            self.cursor.execute(sql_query, (user_name, user_email, user_password, user_type))
            self.db_con.commit()

        except Error as e:
            print(e)

    def user_exists(self, user_email):
        sql_query = 'SELECT * FROM users WHERE email=%s'
        
        try:
            result = self.cursor.execute(sql_query, (user_email))
            return result

        except Error as e:
            print(e)

    def get_existing_user(self, user_email):
        sql_query = 'SELECT * FROM users WHERE email=%s'

        try: 
            self.cursor.execute(sql_query, (user_email))
            result = self.cursor.fetchone()
            
            return result
        
        except Error as e:
            print(e)
