# pip install sqlalchemy-firebird
import configparser
import fdb


class ConectBd:

    # def connection(self):
    #     cfg = configparser.ConfigParser()
    #     cfg.read('cfg.ini')
    #     # String de conexão.
    #     dsn = f"{cfg['DEFAULT']['Host']}:{cfg['DEFAULT']['NomeBanco']}"
    #     # Conectando ao banco de dados.
    #     connection = fdb.connect(dsn=dsn, user=cfg['DEFAULT']['User'], password=cfg['DEFAULT']['Password'], charset='ISO8859_1') # Definir o charset desejado, como UTF8, ISO8859_1, WIN1252
    #
    #     cursor = connection.cursor()
    #     return cursor
    def connection(self):
        try:
            cfg = configparser.ConfigParser()
            cfg.read('cfg.ini')
            # String de conexão.
            dsn = f"{cfg['DEFAULT']['Host']}:{cfg['DEFAULT']['NomeBanco']}"
            # Conectando ao banco de dados.
            connection = fdb.connect(dsn=dsn, user=cfg['DEFAULT']['User'], password=cfg['DEFAULT']['Password'],
                                     charset='ISO8859_1')

            cursor = connection.cursor()
            return cursor
        except Exception as e:
            print("Ocorreu um erro ao conectar ao banco de dados:", e)
            # Retornar None ou relançar a exceção, dependendo da necessidade.
            return None
            # Ou, se preferir, pode descomentar a linha abaixo para relançar a exceção.
            # raise

    def dataForDict(self, cursor, data):
        if data:
            columns = [desc[0] for desc in cursor.description]
            data_dict = {col: data[i] for i, col in enumerate(columns)}
            return data_dict
        else:
            columns = [desc[0] for desc in cursor.description]
            data_dict = {col: None for i, col in enumerate(columns)}
            return data_dict