
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

class ##StepKey##LayoutData:

    def valid(self):
        pass

    def entity(self):
        cursor = conn.connection()
        cursor.execute(f"select * from {table_name}")
        row = cursor.fetchone()
        columns = [desc[0] for desc in cursor.description]
        if not row:
            row = tuple(None for _ in range(len(columns)))
        entity = dict(zip(columns, row))
        return entity

    def exist(self, ##constraints##):
        try:
            cursor = conn.connection()
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
            cursor = conn.connection()
            if 'DATACRIACAO' in column_not_null:
                values = {**values,**_validation.default_log()}
            columns = ", ".join(values.keys())
            value = ", ".join(["?"] * len(values))
            query = f"INSERT INTO ##insert_into## ({columns}) VALUES ({value})"
            cursor.execute(query, tuple(values.values()))
            if not homologacao:
                cursor.connection.commit()
                return "Dado inserido com sucesso!"
            else:
                return "Dado Simulados com sucesso!"
        except Exception as e:
            return f"Erro ao tentar inserir o dado: {e}"

    def save_data(self, table_name, values, line):
        _validation.insert_data(table_name, columns, [values])
        _log.log(f'Linha {line}: ##Msg## foi gravada com sucesso.', filename=table_name)
        return True 
 """,
'layoutReader': """import logging
from Core import imports
from Layout import ##layout##
from LayoutData import ##layout##Data
from Validations import validationData

_entity_##class## = ##layout##.##Class##Layout()
_entity_##class##_data = ##layout##Data.##Class##LayoutData()
_entity = _entity_##class##_data.entity()
_valid = validationData.ValidationData()

utl = imports.util
msg = imports.messages
log = imports.log
type = imports.typeConverter
file = imports.file

#Calculados

class ##Class##LayoutReader:

    def ##class##_reader(self,_column):
        global _entity

        _entity = dict.fromkeys(_entity, None)
        ##entity##
        
        return _entity
      
    def check(self):
        if _entity_##class##_data.exist(##_entity_constraints##):
            log.log(f"A ##Class## com {##_entity_constraints##} já esta gravado.", _entity_##class##.table_name())
            return False
        return True
    
    def valid(self):
        return True
        
    def save(self):
        _entity['ID'] = _valid.last_id(_entity_##class##.table_name())
        _entity_##class##_data.insert_data(_entity)
        
    def run(self, line_data, linha):
        self.##class##_reader(line_data)
        if self.check(linha) and self.valid(linha):
            self.save()
"""
}