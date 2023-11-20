from Validations.validationData import ValidationData
class FornecedorLayout:         
    def table_name(self):
        return 'Fornecedor'    
    def id_table_get(self):
        return []
    
    def table_constraint(self):
        return [] 
        
    def table_foreing_key(self):
        return {'PESSOA': ['CODFORNECEDOR']}
    
    def columns_not_null_get(self):
        return []

    def columns_get(self):
        return [] 