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
            file_name.clear()

def factoryLayoutData():
    for layoutData in core.step:
        file_name = core.step[f'{layoutData}']
        print(file_name)
        table = core.step[f'{layoutData}'][2]
        print(table)
        file_py_dir = struct.create_file_py('LayoutData', file_name=file_name[1]+'Data', content=contentData)

        if file_py_dir != False:
            struct.replace_content_file_py(file_py_dir, '##layout_py##', file_name[1])
            struct.replace_content_file_py(file_py_dir, '##layout_class##', file_name[0])
            struct.replace_content_file_py(file_py_dir, '##StepKey##', file_name[0])


factoryLayoutData()