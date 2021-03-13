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
