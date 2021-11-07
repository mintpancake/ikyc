import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="project")
cursor = conn.cursor()

# sql = "INSERT INTO Login VALUES (%s, %s)"
# val = (1, '2021-11-02-23-58-38')
# cursor.execute(sql, val)
# conn.commit()

sql = "SELECT login_time FROM LoginTime WHERE user_id='%s' ORDER BY login_time DESC" % 1
cursor.execute(sql)
result = cursor.fetchall()
print(result)
