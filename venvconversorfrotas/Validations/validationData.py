import configparser
from Data.conectBd import ConectBd
from datetime import datetime
from Util import util

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')

colum_log_default = ", operadorcriador, datacriacao, operadoratualizador, dataatualizacao"
script_all = 'select * from table'

class ValidationData:

    def operador(self):

        cursor = ConectBd().connection()
        id_operador = cursor.execute( f""" select idoperador from OPERADOR where login = 'esmaster' """ )
        return id_operador.fetchone()[0]

    def default_log(self):

        operador = ValidationData().operador() #criar função para incluir operador no arquivo de configuração.
        data_criacao = datetime.now()
        data_atualizacao = datetime.now()
        log_default = [str(operador), data_criacao, str(operador), data_atualizacao]
        return log_default

    def last_id(self, table):

        id_name = ValidationData().search_id_name(str(table))
        global script_all
        query = script_all.replace('*', f'max({str(id_name).strip()})').replace('table', f'{table}')
        id_name = ''
        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] + 1

    def exist (self, table, values, constraint, upper=False):
        script_all = 'select * from table'
        step = 0
        new_where = ''
        where = dict(zip(constraint, values))
        for constr, val in where.items():
            if upper:
                new_where += f" upper({constr}) = upper('{val}') "
                if step < len(where)-1:
                    new_where += ' and'
                    step +=1
            else:
                new_where += f" {constr} = '{val}' "
                if step < len(where) - 1:
                    new_where += ' and'
                    step += 1
            script_all = script_all + ' where ' + new_where
        script_all = script_all.replace('table', f'{table}')
        # print(script_all)
        cursor = ConectBd().connection()
        cursor.execute(script_all)
        result = cursor.fetchone()
        cursor.close()
        cursor.connection.close()
        return result
    
    def table_description(self, table):
        
        query = f""" SELECT
        rf.RDB$FIELD_NAME AS column_name,
        CASE f.RDB$FIELD_TYPE
        WHEN 7 THEN 'SMALLINT'
        WHEN 8 THEN 'INTEGER'
        WHEN 10 THEN 'FLOAT'
        WHEN 12 THEN 'DATE'
        WHEN 13 THEN 'TIME'
        WHEN 14 THEN 'CHAR'
        WHEN 16 THEN 'BIGINT'
        WHEN 27 THEN 'DOUBLE PRECISION'
        WHEN 35 THEN 'TIMESTAMP'
        WHEN 37 THEN 'VARCHAR'
        WHEN 40 THEN 'CSTRING'
        WHEN 45 THEN 'BLOB_ID'
        WHEN 261 THEN 'BLOB'
        ELSE 'UNKNOWN'
        END AS field_type_name,
        f.RDB$FIELD_LENGTH AS field_length,
        CASE
            WHEN EXISTS (
                SELECT 1
                FROM
                    RDB$RELATION_CONSTRAINTS rc
                JOIN
                    RDB$INDEX_SEGMENTS iseg ON rc.RDB$INDEX_NAME = iseg.RDB$INDEX_NAME
                WHERE
                    rc.RDB$RELATION_NAME = rf.RDB$RELATION_NAME
                    AND iseg.RDB$FIELD_NAME = rf.RDB$FIELD_NAME
                    AND rc.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY'
            ) THEN 'YES'
            ELSE 'NO'
        END AS primary_key,
        CASE
            WHEN rf.RDB$NULL_FLAG = 1 THEN 'YES'
            ELSE 'NO'
        END AS not_null
        FROM
            RDB$RELATION_FIELDS rf
        JOIN
            RDB$FIELDS f ON rf.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME
        WHERE
            rf.RDB$RELATION_NAME = '{table}'
        ORDER BY
        (CASE
            WHEN EXISTS (
                SELECT 1
                FROM
                    RDB$RELATION_CONSTRAINTS rc
                JOIN
                    RDB$INDEX_SEGMENTS iseg ON rc.RDB$INDEX_NAME = iseg.RDB$INDEX_NAME
                WHERE
                    rc.RDB$RELATION_NAME = rf.RDB$RELATION_NAME
                    AND iseg.RDB$FIELD_NAME = rf.RDB$FIELD_NAME
                    AND rc.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY'
            ) THEN 1
            ELSE 2
         END),
        (CASE
            WHEN rf.RDB$NULL_FLAG = 1 THEN 1
            ELSE 2
         END),
        rf.RDB$FIELD_POSITION; """

        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cursor.connection.close()
        return result

    def return_constraint_table(self, table):
        clear = util.Util()
        constrant = []
        query = f""" SELECT
                --rc.RDB$CONSTRAINT_NAME AS constraint_name,
                iseg.RDB$FIELD_NAME AS column_name
            FROM
                RDB$RELATION_CONSTRAINTS rc
            JOIN
                RDB$INDEX_SEGMENTS iseg ON rc.RDB$INDEX_NAME = iseg.RDB$INDEX_NAME
            WHERE
                rc.RDB$CONSTRAINT_TYPE = 'UNIQUE'
                AND rc.RDB$RELATION_NAME = '{table}' """

        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            constrant.append(clear.remove_spaces(i[0]))
        cursor.close()
        cursor.connection.close()
        return constrant

    def search_id_name (self, table):

        query = f"""SELECT r.RDB$FIELD_NAME AS id
                FROM RDB$RELATION_CONSTRAINTS c
                JOIN RDB$INDEX_SEGMENTS s ON c.RDB$INDEX_NAME = s.RDB$INDEX_NAME
                JOIN RDB$RELATION_FIELDS r ON r.RDB$FIELD_NAME = s.RDB$FIELD_NAME
                WHERE c.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY' AND c.RDB$RELATION_NAME = '{table}';
                """
        cursor = ConectBd().connection()
        cursor.execute(query)
        result  = cursor.fetchone()
        cursor.close()
        cursor.connection.close()
        return result[0]
    
    def return_id(self, table):
        global script_all
        id_name = ValidationData().search_id_name(str(table))
        query = str(script_all).replace('*', f'{id_name}'.strip()).replace('table', f'{table}')
        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        cursor.connection.close()
        return result[0]

    def insert_data(self, table, columns, values):
        id_table = ValidationData().last_id(table)
        value_log_default = ValidationData().default_log()
        values = values + value_log_default
        values.insert(0,id_table)
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT INTO {table} ({columns_str}{colum_log_default}) VALUES ({placeholders})"
        try:
            cursor = ConectBd().connection()
            cursor.execute(query, values)
            cursor.connection.commit()
            print("Dados inseridos com sucesso.")
            return True
        except Exception as e:
            cursor.connection.rollback()
            print(f"Ocorreu um erro ao inserir os dados: {e}")
            return False
        finally:
            cursor.close()
            cursor.connection.close()
