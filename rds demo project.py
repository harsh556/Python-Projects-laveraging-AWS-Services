!pip install PyMySQL
import pymysql
db=pymysql.connect(host='database-********************************',user='********',password='********')
cursor = db.cursor()
cursor
cursor.execute("select version()")
data
sql = '''create database hospital'''
cursor.execute(sql)
cursor.connection.commit()
sql = '''use hospital'''
cursor.execute(sql)
sql = '''
create table patient(
sno int not null auto_increment primary key,
pname text,
page text,
psex text,
pBgroup text,
pdoctor text,
pbill text
)'''
cursor.execute(sql)
sql = '''show tables'''
cursor.execute(sql)
cursor.fetchall()
sql = '''
insert into patient(pname, page, pBgroup, pdoctor, pbill)values('%s', '%s', '%s', '%s', '%s')'''%('harsh', '22', 'b+', 'Drvijay', 'two hundred')
cursor.execute(sql)
db.commit()
sql = '''select * from patient'''
cursor.execute(sql)
cursor.fetchall()
    option = input('to see patient details press 1\n')
    if option=='1':
            sql = '''select * from patient'''
            a= cursor.execute(sql)
            b= cursor.fetchall()
            print (b)
    else:
        exit

