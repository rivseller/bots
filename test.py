import MySQLdb
import config

try:
    conn = config.connect

except MySQLdb.Error as err:
    print("Connection error: {}".format(err))
    conn.close()

sql = "SELECT * FROM `visitors` WHERE `unique_key` <30"

try:
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
except MySQLdb.Error as err:
    print("Query error: {}".format(err))

print(data)