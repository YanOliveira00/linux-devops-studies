from psycopg2 import connect

conn = connect(
    dbname=:"yan_db",
    user="yan",
    host="172.17.0.2",
    password = "yan"
)
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM my_table;")
for i, record in enumerate(cursor):
    print("\n", type(record))
    print(record)

cursor.close()
conn.close()
