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

    def log_simples(self):
        return ['operadorcriador', 'datacriacao', 'operadoratualizador', 'dataatualizacao']

    def default_log(self):
        operador = ValidationData().operador()  # Create a function to retrieve the operator from the configuration file.
        data_criacao = datetime.now()
        data_atualizacao = datetime.now()

        log_default = {
            'OPERADORCRIADOR': str(operador),
            'DATACRIACAO': data_criacao,
            'OPERADORATUALIZADOR': str(operador),
            'DATAATUALIZACAO': data_atualizacao
        }

        return log_default

    def last_id(self, table):
        id_name = ValidationData().search_id_name(str(table))
        query = f"select max({str(id_name).strip()}) from {table}"
        id_name = ''
        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchone()
        if not result[0]:
            return 1
        else:
            return result[0] + 1

    def table_PK(self, table):
        clear = util.Util()
        primary_key = []
        query = f""" SELECT RDB$INDEX_SEGMENTS.RDB$FIELD_NAME
                    FROM RDB$INDICES
                    JOIN RDB$RELATION_CONSTRAINTS ON RDB$RELATION_CONSTRAINTS.RDB$INDEX_NAME = RDB$INDICES.RDB$INDEX_NAME
                    JOIN RDB$INDEX_SEGMENTS ON RDB$INDEX_SEGMENTS.RDB$INDEX_NAME = RDB$RELATION_CONSTRAINTS.RDB$INDEX_NAME
                    WHERE RDB$INDICES.RDB$RELATION_NAME = '{table}'
                    AND RDB$RELATION_CONSTRAINTS.RDB$CONSTRAINT_TYPE = 'PRIMARY KEY' """
        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            primary_key.append(clear.remove_spaces(i[0]))
        cursor.close()
        cursor.connection.close()
        return primary_key

    def table_description(self, table):
        query = f""" SELECT
        trim(rf.RDB$FIELD_NAME) AS column_name,
        trim(CASE f.RDB$FIELD_TYPE
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
        END) AS field_type_name,
        trim(f.RDB$FIELD_LENGTH) AS field_length,
        trim(CASE
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
        END) AS primary_key,
        trim(CASE
            WHEN rf.RDB$NULL_FLAG = 1 THEN 'YES'
            ELSE 'NO'
        END) AS not_null
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

    def return_foreign_key(self, table):
        clear = util.Util()
        table = util.Util().to_uppercase(table)
        table_foreign_key = []
        colum_foreign_key = []
        query = f""" SELECT
                distinct
                trim(ref_idx.RDB$RELATION_NAME) AS referenced_table,
                trim(iseg.RDB$FIELD_NAME) AS foreign_key_field
                FROM
                RDB$RELATION_CONSTRAINTS rc
                JOIN RDB$REF_CONSTRAINTS refc ON rc.RDB$CONSTRAINT_NAME = refc.RDB$CONSTRAINT_NAME
                JOIN RDB$INDEX_SEGMENTS iseg ON rc.RDB$INDEX_NAME = iseg.RDB$INDEX_NAME
                JOIN RDB$RELATION_CONSTRAINTS ref_rc ON refc.RDB$CONST_NAME_UQ = ref_rc.RDB$CONSTRAINT_NAME
                JOIN RDB$INDEX_SEGMENTS ref_iseg ON ref_rc.RDB$INDEX_NAME = ref_iseg.RDB$INDEX_NAME
                JOIN RDB$INDICES ref_idx ON ref_rc.RDB$INDEX_NAME = ref_idx.RDB$INDEX_NAME
                WHERE
                rc.RDB$RELATION_NAME = '{table}' AND rc.RDB$CONSTRAINT_TYPE = 'FOREIGN KEY'
                ORDER BY
                ref_idx.RDB$RELATION_NAME; """

        cursor = ConectBd().connection()
        cursor.execute(query)
        result = cursor.fetchall()

        dicionario = {}


        for chave, valor in result:
            if chave in dicionario:
                dicionario[chave].append(valor)
            else:
                dicionario[chave] = [valor]
        if 'OPERADOR' in dicionario:
            del dicionario['OPERADOR']
        return dicionario

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

    def query(self, query):
        cursor = ConectBd().connection()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0].lower() for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def factory_where(self, *args):
        args = args[0]
        step = 1
        new_where = " where "
        if len(args) != 0:
            for where in args:
                if step < len(args):
                    new_where = new_where + where + f" = '{{{where}}}' and "
                    step+=1
                else:
                    new_where = new_where + where + f" = '{{{where}}}' "
                    step += 1
        return new_where
    def factory_exists(self, table, where):
        query = f' select * from {table} {where}'
        return query
    def factory_into(self,table, *args):
        return f""" insert into {table} {args[0]} values (values) """

    def factory_entity(self, table, *args):
        entity = ""

        for i, colum in enumerate(args[0], start=0):

            if colum[1] == 'INTEGER':
                if colum[4] == 'YES':
                    entity = entity +'\n'+(f"        _entity['{colum[0]}']=type.to_integer(_column[{i}]) #obrigatorio")
                else:
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.to_integer(_column[{i}])")
            elif colum[1] == 'VARCHAR':
                if colum[4] == 'YES':
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.to_string(_column[{i}]) #obrigatorio")
                else:
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.to_string(_column[{i}])")

            elif colum[1] == 'DATE':
                if colum[4] == 'YES':
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.string_to_date(_column[{i}]) #obrigatorio")
                else:
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.string_to_date(_column[{i}])")

            elif colum[1] == 'TIMESTAMP':
                if colum[4] == 'YES':
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.string_to_datetime(_column[{i}]) #obrigatorio")
                else:
                    entity = entity + '\n' + (f"        _entity['{colum[0]}']=type.string_to_datetime(_column[{i}])")
        return entity

