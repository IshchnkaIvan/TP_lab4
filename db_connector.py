import mysql.connector
import configparser


class sql_executor:

    def __init__(self, configs_file_name: str) -> None:
        self.configs_file_name = configs_file_name

    def __db_connect(self) -> None:
        config = configparser.ConfigParser()
        config.read(self.configs_file_name)
        conn = mysql.connector.connect(host=config['db_connect']['host'],
                                       database=config['db_connect']['database'],
                                       user=config['db_connect']['user'],
                                       password=config['db_connect']['password'])
        return conn

    def execute_sql_script(self, query: str) -> None:
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

    def count_query(self):
        result = self.execute_sql_script('''
                select count(*)
                from Enrolle 
                where passing_score>250;
                ''')
        return result

    def sum_query(self):
        result = self.execute_sql_script('''
                select sum(CT_rating)
                from Enrolle
                where gender="F";
                ''')
        return result

    def min_max_query(self):
        result = self.execute_sql_script('''
                select max(CT_rating),min(CT_rating)
                from Enrolle;
                ''')
        return result

    def join_query(self):
        result = self.execute_sql_script('''
                select enrolle.id, enrolle.surname, enrolle.`name`, enrolle.middle_name, enrolle.birthdate, university.university_name
                from enrolle 
                left join university ON enrolle.university_id = university.id;
                ''')
        return result

    def select_query(self):
        result = self.execute_sql_script('''
                select *
                from enrolle
                where
                CT_rating > 225;
                ''')
        return result

    def select_all(self):
        result = self.execute_sql_script('''
                select Enrolle.*,University.*
                from Enrolle
                inner join University
                on Enrolle.university_id=University.id
                where University.id=3;    
                ''')
        return result
