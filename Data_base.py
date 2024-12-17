import MySQLdb


# # Replace these with your actual MySQL connection details
host = 'localhost'
user = 'root'
database = 'world'

try:
    conn = MySQLdb.connect(host=host, user=user, passwd="Pandhurna@21", db=database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM country")
    rows = cursor.fetchall()
    print(len(rows))
    print("Connection established")
except:
    print(f"Error")

