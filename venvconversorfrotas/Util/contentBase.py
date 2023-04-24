
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
'layoutData' : """import configparser
import logging
import pandas as pd
import core
from Validations import validationData
from Layout import ##layout_py##
from Util import log, util
import pandas as pd

cfg = configparser.ConfigParser()
cfg.read(r'C:\\Users\Equiplano\PycharmProjects\conversorFrotas\cfg.ini')
path_dir = cfg['DEFAULT']['DiretorioArquivos']
_util = util.Util()
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
columns = column + column_not_null

class ##StepKey##LayoutData:

    def save_data(self, table_name, values, constrant, line):
        if (_validation.exist(table_name, values, constrant, True)) == None:
            _validation.insert_data(table_name, columns, values)
            _log.log(f'Linha {line}: ##Msg## foi gravada com sucesso.', filename=table_name, level=logging.INFO)
            return True
        else:
            _log.log(f'Linha {line}: ##Msg##, já esta gravada.', filename=table_name, level=logging.WARN)
            return False

for line in pd.read_csv(_path_file, chunksize=1, header=None):
    line_index = line.index.stop #identificação da linha no arquivo
    values = line.values[0][0].split('|')
    ##campo## = values[0]
    _instanceLayoutData = ##layout_class##LayoutData()
    _instanceLayoutData.save_data(table_name, [##campo##], constrant, line_index) """
}