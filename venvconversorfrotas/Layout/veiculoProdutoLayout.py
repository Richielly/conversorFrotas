from Validations.validationData import ValidationData
class VeiculoProdutoLayout:         
    def table_name(self):
        return 'SCF_VEICULOPRODUTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoProdutoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoProdutoLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULO', 'IDPRODUTO']

    def columns_get(self):
        return [] 