import mysql.connector

conn = mysql.connector.connect(user='root', password='my-secret-pw', host='127.0.0.1')
cursor = conn.cursor()

def create_database(dbname):
    cursor.execute("DROP database IF EXISTS {}".format(dbname))
    sql = "CREATE database {}".format(dbname)
    cursor.execute(sql)
    conn.close()
    return cursor

def show_database():
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())
    conn.close()

def create_table(table,schema):
    cursor.execute("DROP table IF EXISTS {}".format(table))
    cursor.execute("CREATE TABLE {} ({})".format(table,schema))
    conn.close()

def show_table():
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())
    conn.close()

def query_table(table):
    cursor.execute("SELECT * FROM {}".format(table))
    print(cursor.fetchall())
    conn.close()

def insert_table(table, columns, values):
    cursor.execute("INSERT INTO {} ({}) VALUES ({})".format(table,columns,values))
    conn.close()
def update_table(table, values):
    cursor.execute("UPDATE {}".format(table,values))
def delete_table(table, ):

if __name__ == '__main__':
    testdb = "testdatabase"
    table = "test"
    schema = "name VARCHAR(255), address VARCHAR(255)"
    create_database(testdb)
    crete_table(table,schema)
    show_database()






