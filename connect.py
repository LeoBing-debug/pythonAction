 
 
# import module
import cx_Oracle as oracle
 
# connect oracle database
db = oracle.connect('scott/redhat@192.168.223.138:1521/oracle.test')
 
# create cursor
cursor = db.cursor()
 
# execute sql
cursor.execute('select sysdate from dual')
 
# fetch data
data = cursor.fetchone()
 
print('Database time:%s' % data)
 
# close cursor and oracle
cursor.close()
db.close()

class testt():
    test3();

def test3():
    print("test3")