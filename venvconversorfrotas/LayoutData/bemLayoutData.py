import configparser
import logging
import os

import pandas as pd
from Core import core
from Data import conectBd
from Validations import validationData
from Layout import bemLayout
from Util import log, util, typeConverter
cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
path_dir = cfg['DEFAULT']['diretorioarquivos']
_util = util.Util()
_converter = typeConverter.TypeConverter()
_core = core.Core
_validation = validationData.ValidationData()
_layout = bemLayout.BemLayout()
_log = log.Log()
_path_file = path_dir + _core.step['Bem'][3]

table_name = _layout.table_name()
next_id = _validation.last_id(table_name)
constrant = _layout.table_constraint()
column = _layout.columns_get()
column_not_null = _layout.columns_not_null_get()
columns = column_not_null + column

conn = conectBd.ConectBd()

class BemLayoutData:

    def valid(self):
        pass

    def entity(self):
        cursor = conn.connection()
        if cursor:
            cursor.execute(f"select * from {table_name}")
            row = cursor.fetchone()
            columns = [desc[0] for desc in cursor.description]
            if not row:
                row = tuple(None for _ in range(len(columns)))
            entity = dict(zip(columns, row))
            return entity

    def exist(self, CODENTIDADE, CODBEM):
        try:
            cursor = conn.connection()
            script = f" select * from SCP55_BEM  where CODENTIDADE = '{CODENTIDADE}' and CODBEM = '{CODBEM}' "
            cursor.execute(script)
            result = cursor.fetchone()
            if result:
                data_dict = conn.dataForDict(cursor, result)
            else:
                data_dict = None
            return data_dict
        except Exception as e:
            _log.log(msg=f"Ocorreu um erro ao consultar o banco de dados SCP55_BEM: {e}")
            print(f"Ocorreu um erro ao consultar o banco de dados {table_name}: {e}")
            return {}
        
    def insert_data(self, values, homologacao=False):
        try:
            cursor = conn.connection()
            if 'DATACRIACAO' in column_not_null:
                values = {**values,**_validation.default_log()}
            columns = ", ".join(values.keys())
            value = ", ".join(["?"] * len(values))
            query = f"INSERT INTO SCP55_BEM ({columns}) VALUES ({value})"
            cursor.execute(query, tuple(values.values()))
            if not homologacao:
                cursor.connection.commit()
                return True
            else:
                return "Dado Simulados com sucesso!"
        except Exception as e:
            _log.log(msg=f"Erro ao tentar inserir o dado na tabela SCP55_BEM: {e}")

    def save_data(self, table_name, values, line):
        _validation.insert_data(table_name, columns, [values])
        _log.log(f'Linha {line}: ##Msg## foi gravada com sucesso.', filename=table_name)
        return True 
 