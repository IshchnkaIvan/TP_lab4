from unittest import TestCase
from db_connector import sql_executor


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
