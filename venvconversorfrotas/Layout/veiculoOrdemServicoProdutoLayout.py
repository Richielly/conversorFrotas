from Validations.validationData import ValidationData
class VeiculoOrdemServicoProdutoLayout:         
    def table_name(self):
        return 'SCF_VEICULOORDEMSERVICOPRODUTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoOrdemServicoProdutoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDVEICULOORDEMSERVICO', 'NRSEQUENCIAPRODUTO'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoOrdemServicoProdutoLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULOORDEMSERVICOPRODUTO', 'IDVEICULOORDEMSERVICO', 'VLQUANTIDADE', 'VLTOTAL', 'IDPRODUTO', 'NRSEQUENCIAPRODUTO']

    def columns_get(self):
        return ['DSOBSERVACAO', 'NRDIASGARANTIA'] 