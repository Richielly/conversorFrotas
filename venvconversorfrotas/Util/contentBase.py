
contentBase = {
    'layout' : """from Validations.validationData import ValidationData
class ##NomeArquivoTabela##Layout:         
    def table_name(self):
        return '##NomeTabela##'    
    def id_table_get(self):
        return ##primaryKey##
    
    def table_constraint(self):
        return ##constraints## 
        
    def table_foreing_key(self):
        return ##foreingKey##
    
    def columns_not_null_get(self):
        return ##columnsNotNull##

    def columns_get(self):
        return ##columns## """,

'layoutData': """import configparser
import logging
import pandas as pd
import core
from Data import conectBd
from Validations import validationData
from Layout import ##layout_py##
from Util import log, util, typeConverter
import pandas as pd

cfg = configparser.ConfigParser()
cfg.read(r'C:\\Users\Equiplano\PycharmProjects\conversorFrotas\cfg.ini')
path_dir = cfg['DEFAULT']['DiretorioArquivos']
_util = util.Util()
_converter = typeConverter.TypeConverter()
_core = core.Core
_validation = validationData.ValidationData()
_layout = ##layout_py##.##layout_class##Layout()
_log = log.Log()
_path_file = path_dir + _core.step['##StepKey##'][3]

table_name = _layout.table_name()
next_id = _validation.last_id(table_name)
constrant = _layout.table_constraint()
column = _layout.columns_get()
column_not_null = _layout.columns_not_null_get()
columns = column_not_null + column

conn = conectBd.ConectBd()
cursor = conn.connection()

class ##StepKey##LayoutData:

    def valid(self):
        pass

    def entity(self):
        global cursor
        cursor.execute(f"select * from {table_name}")
        _entity = cursor.description

        return _entity

    def exist(self, ##constraints##):
        try:
            global cursor
            script = f"##select_exist##"
            cursor.execute(script)
            result = cursor.fetchone()
            if result:
                data_dict = conn.dataForDict(cursor, result)
            else:
                data_dict = None
            return data_dict
        except Exception as e:
            print(f"Ocorreu um erro ao consultar o banco de dados: {e}")
            return {}
        
    def insert_data(self, values, homologacao=False):
        try:
            if 'OPERADORCRIADOR' in column_not_null:
                values = {**values,**_validation.default_log()}
            columns = ", ".join(values.keys())
            value = ", ".join(["?"] * len(values))
            query = f"INSERT INTO ##insert_into## ({columns}) VALUES ({value})"
            cursor.execute(query, tuple(values.values()))
            if not homologacao:
                cursor.connection.commit()
                print("Dado inserido com sucesso!")
            else:
                print("Dado Simulados com sucesso!")
        except Exception as e:
            print(f"Erro ao tentar inserir o dado: {e}")

    def save_data(self, table_name, values, line):
        _validation.insert_data(table_name, columns, [values])
        _log.log(f'Linha {line}: ##Msg## foi gravada com sucesso.', filename=table_name, level=logging.INFO)
        return True 
 """,
'layoutReader': """import logging
from Core import imports
from Layout import ##class##Layout
from LayoutData import ##layout##Data
_entity_##class## = ##class##Layout.##Class##Layout()
_entity_##class##_data = ##class##LayoutData.##Class##LayoutData()
utl = imports.util
msg = imports.messages
log = imports.log
class ##Class##LayoutReader:

    def ##class##_reader(self):
        pass
      
    def check(self):
        global _entity_##class##
        global _entity_##class##_data
        if _entity_##class##_data.exist(##constraints##):
            log.log(f'A ##Class## com {##constraints##} já existe.', _entity_##class##.table_name(), logging.INFO)
            return False
        return True
        
teste = ClasseLayoutReader()
print(teste.check())
"""
}