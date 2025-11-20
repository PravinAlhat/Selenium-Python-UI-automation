import mysql.connector

def connect_to_db():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Automationdb@77',
            database='product',
            use_pure=False
        )
        print("Connection established successfully")
        if 'cnx' in locals() and cnx.is_connected():
            cursor = cnx.cursor()
        return cursor
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    