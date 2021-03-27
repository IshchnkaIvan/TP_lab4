from unittest import TestCase
import main


class TestEnrolle(TestCase):
    connector = main.ORMConnector()

    def test_count_query(self):
        self.assertEqual(self.connector.count_query(), 3)

    def test_min_max_query(self):
        self.assertEqual(self.connector.min_max_query(), (382, 350))

    def test_sum_query(self):
        self.assertEqual(self.connector.sum_query(), 746)

    def test_join_query(self):
        self.assertEqual(self.connector.join_query(), [])

    def test_select_query(self):
        self.assertEqual(self.connector.select_query(),
                         [('1', 'Belevich', 'Mikhail', 'Andreevich', 'M', 'belarussian', '0000-00-00', '246000,Belarus,Gomel,International street,15,7', '382', '364', 'None'),
 ('2', 'Ishchenko', 'Ivan', 'Sergeevich', 'M', 'belarussian', '0000-00-00', '246000,Belarus,Gomel,Portovaya street,51', '364', '364', 'None'),
 ('3', 'Korolko', 'Olga', 'Yurievna', 'F', 'belarussian', '0000-00-00', '246000,Belarus,Pinsk,Krasnoflotskaya 8,2', '350', '328', 'None')])
