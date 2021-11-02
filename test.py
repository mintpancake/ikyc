import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="ikyc")
cursor = conn.cursor()

# sql = "INSERT INTO Login VALUES (%s, %s)"
# val = (1, '2021-11-02-23-58-38')
# cursor.execute(sql, val)
# conn.commit()

sql = "SELECT * FROM Login"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

sql = "DELETE FROM Login WHERE login_time = '2021-11-3-0-16-13'"
cursor.execute(sql)
conn.commit()