from unittest import TestCase
import main


class TestEnrolle(TestCase):
    connector = main.ORMConnector()

    def test_count_query(self):
        self.assertEqual(self.connector.count_query(), 3)

    def test_min_max_query(self):
        self.assertEqual(self.connector.min_max_query(), (350, 382))
