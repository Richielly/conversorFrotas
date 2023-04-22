from Validations.validationData import ValidationData
class NfProdutoLayout:         
    def table_name(self):
        return 'SCF_NFPRODUTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = NfProdutoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = NfProdutoLayout()
        id = id_bem.id_name_get()
        return ['IDPRODUTONFABASTECIMENTO', 'IDNF']

    def columns_get(self):
        return ['IDPRODUTO', 'PRECOAJUSTADO'] 