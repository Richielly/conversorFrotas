import configparser
import logging
import core
from Validations import validationData
from Layout import corLayout
from Util import log, util
import pandas as pd

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
path_dir = cfg['DEFAULT']['DiretorioArquivos']
_util = util.Util()
_core = core.Core
_validation = validationData.ValidationData()
_layout = corLayout.CorLayout()
_log = log.Log()
class CorLayoutData:

    path_data = path_dir + _core.step['Cor'][3]

    import pandas as pd

    def __int__(self):
        self.table_name = _layout.table_name()
        self.next_id = _validation.last_id(self.table_name)
        self.constrant = _layout.table_constraint()
        self.column = _layout.columns_get()
        self.column_not_null = _layout.columns_not_null_get()
        self.columns = self.column + self.column_not_null

    def exists_data(self, table_name, values, constrant):
        if _validation.exist(table_name, values, constrant, upper=True) != None:
            _log.log(f'A cor "{values}", já esta gravada.', filename=table_name, level=logging.WARN)
            return True
        else:
            _log.log(f'Cor "{values}", gravada com sucesso.', filename=table_name, level=logging.INFO)
            return False
    def save_data(self, values):
        _validation.insert_data(self.table_name, self.columns, values)

arquivo = path_dir + "Cor.txt"
chunksize = 1

for chunk in pd.read_csv(arquivo, chunksize=chunksize, header=None):
    print(str(chunk.values[0][0]).split('|')[0])

