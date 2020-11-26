import pymysql

con = pymysql.connect('localhost', 'root', 'root', 'online_store')
cur = con.cursor()
