import mysql.connector
import configparser


class sql_executor:

    def __init__(self, configs_file_name: str) -> None:
        self.configs_file_name = configs_file_name

    def __db_connect(configs_file_name: str) -> None:
        config = configparser.ConfigParser()
        config.read('configs.txt')
        conn = mysql.connector.connect(host=config['db_connect']['host'],
                                       database=config['db_connect']['database'],
                                       user=config['db_connect']['user'],
                                       password=config['db_connect']['password'])
        return conn

    def execute_sql_script(self, sql_file_name: str) -> None:
        try:
            conn = self.__db_connect(self.configs_file_name)
            cursor = conn.cursor()
            with open(sql_file_name) as sql_file:
                for _ in cursor.execute(sql_file.read(), multi=True):
                    pass
            conn.commit()
        except Exception as e:
            print(e)

        finally:
            conn.close()
            cursor.close()
