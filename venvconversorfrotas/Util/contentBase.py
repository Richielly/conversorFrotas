
contentBase = {
    'layout' : """from Validations.validationData import ValidationData
class ##NomeArquivoTabela##Layout:         
    def table_name(self):
        return '##NomeTabela##'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ##NomeArquivoTabela##Layout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ##constraints## #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ##NomeArquivoTabela##Layout()
        id = id_bem.id_name_get()
        return ##columnsNotNull##

    def columns_get(self):
        return ##columns## """,

'layoutData': """import configparser
import logging
import pandas as pd
import core
from Data.conectBd import ConectBd
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

class ##StepKey##LayoutData:

    def valid(self):
        pass

    def entity(self):
        _entity = []
        _entity.append(_converter.to_string('#'))
        _entity.append(_converter.to_integer('#'))

        return _entity

    def exist(self, *args):
        cursor = ConectBd().connection()
        script = f"##select_exist##"
        cursor.execute(script)
        result = cursor.fetchone()
        cursor.close()
        cursor.connection.close()
        return result

    def insert_data(self, values):
        id = _validation.last_id(table_name)
        values.insert(0,id)
        query = "##insert_into##"
        cursor.execute(query)
        cursor.close()
        cursor.connection.close()

    def save_data(self, table_name, values, line):
        _validation.insert_data(table_name, columns, [values])
        _log.log(f'Linha {line}: ##Msg## foi gravada com sucesso.', filename=table_name, level=logging.INFO)
        return True
###################Tirar do Layout padrao #######################
for line in pd.read_csv(_path_file, chunksize=1, header=None):
    line_index = line.index.stop #identificacao da linha no arquivo
    values = line.values[0][0].split('|')
    nmEspecie = values[0]
    tpEspecieAcumulador = values[1]
    tpCategoriaCnh = values[2]
    tpVeiculoTce = values[4]
 
 """
}