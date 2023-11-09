# pip install sqlalchemy-firebird
import configparser
import fdb

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')

class ConectBd:

    def connection(self):
        # String de conexão.
        dsn = f"{cfg['DEFAULT']['Host']}:{cfg['DEFAULT']['NomeBanco']}"
        # Conectando ao banco de dados.
        connection = fdb.connect(dsn=dsn, user=cfg['DEFAULT']['User'], password=cfg['DEFAULT']['Password'], charset='ISO8859_1') # Definir o charset desejado, como UTF8, ISO8859_1, WIN1252

        cursor = connection.cursor()
        return cursor

    def dataForDict(self, cursor, data):
        if data:
            columns = [desc[0] for desc in cursor.description]
            data_dict = {col: data[i] for i, col in enumerate(columns)}
            return data_dict
        else:
            columns = [desc[0] for desc in cursor.description]
            data_dict = {col: None for i, col in enumerate(columns)}
            return data_dict