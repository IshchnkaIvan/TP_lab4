from unittest import TestCase

import db_connector
from db_connector import sql_executor


class TestsqlExecutor(TestCase):
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
        self.assertEqual(int(result[0][0]), 350)

class TestDbConnector(TestCase):

    def test_count_query(self):
        cursor = sql_executor('configs.txt')
        self.assertEqual(cursor.count_query()[0][0], 3)

    def test_min_max_query(self):
        cursor = sql_executor('configs.txt')
        self.assertEqual(cursor.min_max_query()[0], (382, 350))

    def test_sum_query(self):
        cursor = sql_executor('configs.txt')
        self.assertEqual(cursor.sum_query()[0][0], 350)

    def test_join_query(self):
        cursor = sql_executor('configs.txt')
        self.assertEqual(cursor.join_query(), [(1, 'Belevich', 'Mikhail', 'Andreevich', None, None),
                (2, 'Ishchenko', 'Ivan', 'Sergeevich', None, None),
                (3, 'Korolko', 'Olga', 'Yurievna', None, None)])

    def test_select_query(self):
        cursor = sql_executor('configs.txt')
        result = [(1,
              'Belevich',
              'Mikhail',
              'Andreevich',
              'M',
              'belarussian',
              None,
              '246000,Belarus,Gomel,International street,15,7',
              382,
              364,
              None),
             (2,
              'Ishchenko',
              'Ivan',
              'Sergeevich',
              'M',
              'belarussian',
              None,
              '246000,Belarus,Gomel,Portovaya street,51',
              364,
              364,
              None),
             (3,
              'Korolko',
              'Olga',
              'Yurievna',
              'F',
              'belarussian',
              None,
              '246000,Belarus,Pinsk,Krasnoflotskaya 8,2',
              350,
              328,
              None)]
        self.assertEqual(cursor.select_query(), result)
