
import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="face_recognizer")
my_cursor=conn.cursor()
Dep='csee'
Teacher='gayal'
Std_id='8'

query='update student set Dep="%s",Teacher="%s" where Std_id="%s"'%(Dep,Teacher,Std_id)
my_cursor.execute(query)
data=my_cursor.fetchall()
conn.commit()
