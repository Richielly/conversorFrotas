from Util import contentBase, base
from Core import core
from Validations import validationData
from Util import util

struct = base.Base()
core = core.Core()
valid = validationData.ValidationData()
content = contentBase.contentBase
contentData = contentBase.contentBase
utl = util.Util()
content = content['layout']
contentData = contentData['layoutData']

def columns_not_null_list(table):
    valid.table_description(table)
    columns_not_null = []
    for col in valid.table_description(table):
        if utl.remove_spaces(col[4]) == 'YES':
            columns_not_null.append(utl.remove_spaces(col[0]))
    list_columns_not_null = utl.remove_itens_in_list(columns_not_null,['OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO'])

    return list_columns_not_null

def columns_list(table):
    columns = []
    for col in valid.table_description(table):
        if utl.remove_spaces(col[4]) == 'NO':
            columns.append(utl.remove_spaces(col[0]))

    list_columns = utl.remove_itens_in_list(columns,['OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO'])
    return list_columns

def constrant_list(table):
    constrant = []
    constrant = valid.return_constraint_table(table)
    return constrant

def factoryLayout():
    for layout in core.step:
        file_name = core.step[f'{layout}']
        table = core.step[f'{layout}'][2]
        file_py_dir = struct.create_file_py('Layout', file_name=file_name[1], content=content)
        if file_py_dir != False:
            struct.replace_content_file_py(file_py_dir, '##NomeArquivoTabela##', file_name[0])
            struct.replace_content_file_py(file_py_dir, '##NomeTabela##', file_name[2])
            struct.replace_content_file_py(file_py_dir, '##constraints##', str(valid.return_constraint_table(file_name[2])))
            struct.replace_content_file_py(file_py_dir, '##columnsNotNull##', str(columns_not_null_list(table)))
            struct.replace_content_file_py(file_py_dir, '##columns##', str(columns_list(table)))
            struct.replace_content_file_py(file_py_dir, '##foreingKey##', str(valid.return_foreign_key(table)))
            file_name.clear()

def factoryLayoutData():
    for layoutData in core.step:
        file_name = core.step[f'{layoutData}']
        table = core.step[f'{layoutData}'][2]
        file_py_dir = struct.create_file_py('LayoutData', file_name=file_name[1]+'Data', content=contentData)

        if file_py_dir != False:
            columns = columns_not_null_list(table) + columns_list(table) + valid.log_simples()
            where = valid.return_constraint_table(file_name[2])
            where = tuple(where)
            where = valid.factory_where(where)
            exists = valid.factory_exists(table,where)
            struct.replace_content_file_py(file_py_dir, '##layout_py##', file_name[1])
            struct.replace_content_file_py(file_py_dir, '##layout_class##', file_name[0])
            struct.replace_content_file_py(file_py_dir, '##StepKey##', file_name[0])
            struct.replace_content_file_py(file_py_dir, '##insert_into##', valid.factory_into(table, tuple(columns)))
            struct.replace_content_file_py(file_py_dir, '##select_exist##', exists)
            file_name.clear()

factoryLayout()
# factoryLayoutData()