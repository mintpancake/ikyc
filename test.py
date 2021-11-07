import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="project")
cursor = conn.cursor()

# sql = "INSERT INTO Login VALUES (%s, %s)"
# val = (1, '2021-11-02-23-58-38')
# cursor.execute(sql, val)
# conn.commit()

sql = "SELECT balance FROM Account WHERE user_id='1' AND account_id='1';"
cursor.execute(sql)
result = cursor.fetchall()[0][0]
print(result)
