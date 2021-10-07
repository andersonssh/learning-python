import mysql.connector
from random import randint


cnx = mysql.connector.connect(user='root',
                                  host='localhost',
                                  database='meu',
                                  password='')

cursor = cnx.cursor()


valores = "insert into teste values (default, 'aki foi no py', '88888');"
tabelas = {}

tabelas['testezao1'] = """
                        create table testezao1(
                            id int auto_increment not null primary key,
                            nome varchar(30) unique,
                            numero int
                        );

                      """
cursor.execute('drop table testezao1;')
cursor.execute(tabelas['testezao1'])

def insert_data():
    with open('nomes.csv', 'r') as nomes:
        for i in range(100000):
            try:
                cursor.execute("insert into testezao1 values (default, '{}', '{}');".format(i, randint(1,1000000)))
            except:
                print('Ops')


insert_data()
cnx.commit()
cursor.close()
cnx.close()
