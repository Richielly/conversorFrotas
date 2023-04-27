# pip install sqlalchemy-firebird
import configparser
import fdb

cfg = configparser.ConfigParser()
cfg.read(r'C:\Users\Equiplano\PycharmProjects\conversorFrotas\cfg.ini')

class ConectBd:

    def connection(self):
        # String de conexão.
        dsn = f"{cfg['DEFAULT']['Host']}:{cfg['DEFAULT']['NomeBanco']}"
        # Conectando ao banco de dados.
        connection = fdb.connect(dsn=dsn, user=cfg['DEFAULT']['User'], password=cfg['DEFAULT']['Password'])
        cursor = connection.cursor()
        return cursor
    #
    # def consulta_para_dict(self, query):
    #     dsn = f"{cfg['DEFAULT']['Host']}:{cfg['DEFAULT']['NomeBanco']}"
    #     conn = fdb.connect(dsn=dsn, user=cfg['DEFAULT']['User'], password=cfg['DEFAULT']['Password'])
    #     cursor = conn.cursor()
    #     cursor.execute(query)
    #     rows = cursor.fetchall()
    #     columns = [desc[0].lower() for desc in cursor.description]
    #     return [dict(zip(columns, row)) for row in rows]

