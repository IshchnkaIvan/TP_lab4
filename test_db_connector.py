from unittest import TestCase
import db_connector

class Testsql_executor(TestCase):
    def test_execute_sql_script(self):
        cursor = db_connector.sql_executor('configs.txt')
        cursor.execute_sql_script('''drop table if exists enrolle;''')
        cursor.execute_sql_script('''
        create table if not exists Enrolle
        (
            id              int          unsigned auto_increment,
            surname         nvarchar(30),
            `name`          nvarchar(20),
            middle_name     nvarchar(20),
            gender          nvarchar(1),
            nationality     nvarchar(30),
            birthdate       date,
            home_address    nvarchar(256),
            CT_rating       smallint     unsigned,
            passing_score   smallint     unsigned,
            primary key (id)
        );''')
        cursor.execute_sql_script('''
        insert into Enrolle (surname, `name`, middle_name, gender, nationality, birthdate, home_address, CT_rating, passing_score)
        	values("Belevich","Mikhail","Andreevich","M","belarussian",
        			01/24/2002,"246000,Belarus,Gomel,International street,15,7",382,364),
                    ("Ishchenko","Ivan","Sergeevich","M","belarussian",
        			18/03/2002,"246000,Belarus,Gomel,Portovaya street,51",364,364),
                    ("Korolko","Olga","Yurievna","F","belarussian",
        			23/10/2001,"246000,Belarus,Pinsk,Krasnoflotskaya 8,2",350,328);
        ''')
        result = cursor.execute_sql_script('''
        select sum(CT_rating)
        from Enrolle
        where gender="F";''')
        self.assertEqual(int(result[0][0]),350)

