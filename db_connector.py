import mysql.connector
import configparser
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')


class Enrolle:

    def __init__(self, id: int = None, surname: str = None, name: str = None, middle_name: str = None,
                 gender: str = None,
                 nationality: str = None, birthdate: str = None, home_address: str = None, CT_rating: int = None,
                 passing_score: int = None, university_id: int = None) -> None:
        self.id: int = id
        self.surname: str = surname
        self.name: str = name
        self.middle_name: str = middle_name
        self.gender: str = gender
        self.nationality: str = nationality
        self.birthdate: str = birthdate
        self.home_address: str = home_address
        self.CT_rating: int = CT_rating
        self.passing_score: int = passing_score
        self.university_id: int = university_id

    def __repr__(self):
        return str((self.id, self.surname, self.name, self.middle_name, self.gender, self.nationality, self.birthdate,
                    self.home_address, self.CT_rating, self.passing_score, self.university_id))


class University:

    def __init__(self, id: int = None, university_name: str = None, university_description: str = None) -> None:
        self.id = id
        self.university_name = university_name
        self.university_description = university_description

    def __repr__(self):
        return str((self.id, self.university_name, self.university_description))


class SqlExecutor:

    def __init__(self, configs_file_name: str) -> None:
        self.configs_file_name = configs_file_name

    def __db_connect(self) -> mysql.connector:
        config = configparser.ConfigParser()
        config.read(self.configs_file_name)
        conn = mysql.connector.connect(
            host=config['db_connect']['host'],
            database=config['db_connect']['database'],
            user=config['db_connect']['user'],
            password=config['db_connect']['password']
        )
        return conn

    def execute_sql_script(self, query: str) -> list[T]:
        try:
            conn = self.__db_connect()
            cursor = conn.cursor()
            cursor.execute(query)
            results_of_query = cursor.fetchall()
            conn.commit()
            return results_of_query
        except Exception as e:
            print(e)

        finally:
            conn.close()
            cursor.close()

    def count_query(self) -> int:
        result = self.execute_sql_script('''
            select count(*)
            from Enrolle 
            where passing_score>250;
            ''')
        return result[0][0]

    def sum_query(self) -> int:
        result = self.execute_sql_script('''
            select sum(CT_rating)
            from Enrolle
            where gender="F";
            ''')
        return result[0][0]

    def min_max_query(self) -> tuple[int, int]:
        result = self.execute_sql_script('''
            select max(CT_rating),min(CT_rating)
            from Enrolle;
            ''')
        return result[0]

    def join_query(self) -> list[Enrolle]:
        result = self.execute_sql_script('''
            select enrolle.id, enrolle.surname, enrolle.`name`, enrolle.middle_name, enrolle.birthdate, university.university_name
            from enrolle 
            left join university ON enrolle.university_id = university.id;
            ''')
        enrolles = [Enrolle(id=id, surname=surname, name=name, middle_name=middle_name, birthdate=birthdate,
                            university_id=university_id) for id, surname, name, middle_name, birthdate, university_id in
                    result]
        return enrolles

    def select_query(self) -> list[Enrolle]:
        result = self.execute_sql_script('''
            select *
            from enrolle
            where
            CT_rating > 225;
            ''')
        enrolles = [enrolle for enrolle in result]
        return enrolles

    def select_all(self) -> list[tuple[Enrolle, University]]:
        results = self.execute_sql_script('''
            select Enrolle.*,University.*
            from Enrolle
            inner join University
            on Enrolle.university_id=University.id
            where University.id=3;    
            ''')
        enrolles_and_universities = [tuple(Enrolle(result[:11]), University(result[11:])) for result in results]
        return enrolles_and_universities
