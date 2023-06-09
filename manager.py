from Util import contentBase, base
from Core import core
from Validations import validationData
from Util import util

struct = base.Base()
core = core.Core()
valid = validationData.ValidationData()
content = contentBase.contentBase
contentData = contentBase.contentBase
contentReader = contentBase.contentBase
utl = util.Util()
content = content['layout']
contentData = contentData['layoutData']
contentReader = contentReader['layoutReader']

class Manager:

    def columns_not_null_list(self, table):
        valid.table_description(table)
        columns_not_null = []
        for col in valid.table_description(table):
            if utl.remove_spaces(col[4]) == 'YES':
                columns_not_null.append(utl.remove_spaces(col[0]))

        return columns_not_null

    def columns_list(self, table):
        columns = []
        for col in valid.table_description(table):
            if utl.remove_spaces(col[4]) == 'NO':
                columns.append(utl.remove_spaces(col[0]))
        return columns

    def constrant_list(self, table):
        constrant = []
        constrant = valid.return_constraint_table(table)
        return constrant

    def fk_list(self, table):
        fk = valid.return_foreign_key(table)
        for chave, valor in fk.items():
            for coluna in valor:
                if coluna in self.columns_not_null_list(table):
                    print(chave, valor)

    def factoryLayout(self):
        for layout in core.step:
            file_name = core.step[f'{layout}']
            table = core.step[f'{layout}'][2]
            file_py_dir = struct.create_file_py('Layout', file_name=file_name[1], content=content)
            constraints = valid.table_PK(table) if not valid.return_constraint_table(file_name[2]) else valid.return_constraint_table(file_name[2])
            if file_py_dir != False:
                struct.replace_content_file_py(file_py_dir, '##NomeArquivoTabela##', file_name[0])
                struct.replace_content_file_py(file_py_dir, '##NomeTabela##', file_name[2])
                struct.replace_content_file_py(file_py_dir, '##constraints##', str(constraints))
                struct.replace_content_file_py(file_py_dir, '##columnsNotNull##', str(self.columns_not_null_list(table)))
                struct.replace_content_file_py(file_py_dir, '##columns##', str(self.columns_list(table)))
                struct.replace_content_file_py(file_py_dir, '##primaryKey##', str(valid.table_PK(table)))
                struct.replace_content_file_py(file_py_dir, '##foreingKey##', str(valid.return_foreign_key(table)))
                file_name.clear()

    def factoryLayoutData(self):
        for layoutData in core.step:
            file_name = core.step[f'{layoutData}']
            table = core.step[f'{layoutData}'][2]
            file_py_dir = struct.create_file_py('LayoutData', file_name=file_name[1]+'Data', content=contentData)
            constraints = valid.table_PK(table) if not valid.return_constraint_table(file_name[2]) else valid.return_constraint_table(file_name[2])
            if file_py_dir != False:
                where = valid.return_constraint_table(file_name[2])
                where = tuple(where)
                where = valid.factory_where(where)
                exists = valid.factory_exists(table,where)
                struct.replace_content_file_py(file_py_dir, '##layout_py##', file_name[1])
                struct.replace_content_file_py(file_py_dir, '##layout_class##', file_name[0])
                struct.replace_content_file_py(file_py_dir, '##StepKey##', file_name[0])
                struct.replace_content_file_py(file_py_dir, '##insert_into##', table)
                struct.replace_content_file_py(file_py_dir, '##select_exist##', exists)
                struct.replace_content_file_py(file_py_dir, '##constraints##', utl.remove_chars(str(constraints),["[", "]", "'"]))
                file_name.clear()
                # self.fk_list(table)

    def factoryLayoutReader(self):
        for layoutData in core.step:
            file_name = core.step[f'{layoutData}']
            table = core.step[f'{layoutData}'][2]
            file_py_dir = struct.create_file_py('LayoutReader', file_name=file_name[1]+'Reader', content=contentReader)
            constraints = valid.table_PK(table) if not valid.return_constraint_table(file_name[2]) else valid.return_constraint_table(file_name[2])

            if file_py_dir != False:
                struct.replace_content_file_py(file_py_dir, '##layout##', file_name[1])
                struct.replace_content_file_py(file_py_dir, '##Class##', file_name[0])
                struct.replace_content_file_py(file_py_dir, '##class##', utl.to_lowercase(file_name[0]))
                struct.replace_content_file_py(file_py_dir, '##constraints##', str(constraints))
                struct.replace_content_file_py(file_py_dir, '##_entity_constraints##', str(constraints).replace("['", "_entity['").replace("', '", "'], _entity['"))
                struct.replace_content_file_py(file_py_dir, '##entity##', utl.remove_chars(str(valid.factory_entity(table,valid.table_description(table))),['"',',']))

# Manager().factoryLayout()
# Manager().factoryLayoutData()
Manager().factoryLayoutReader()
