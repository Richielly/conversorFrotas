from Validations.validationData import ValidationData
class ClassificacaoFornecedorLayout:         
    def table_name(self):
        return 'SCF_CLASSIFICACAOFORNECEDOR'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ClassificacaoFornecedorLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'CODFORNECEDOR', 'TPCLASSIFICACAOFORNECEDOR'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ClassificacaoFornecedorLayout()
        id = id_bem.id_name_get()
        return ['IDCLASSIFICACAOFORNECEDOR', 'CODENTIDADE', 'CODFORNECEDOR']

    def columns_get(self):
        return ['TPCLASSIFICACAOFORNECEDOR'] 