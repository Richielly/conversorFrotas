
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

    'layoutData' : """  """
}