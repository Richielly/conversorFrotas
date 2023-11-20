from Validations.validationData import ValidationData
class GrupoLayout:         
    def table_name(self):
        return 'GRUPO'    
    def id_table_get(self):
        return ['CODGRUPO']
    
    def table_constraint(self):
        return ['CODGRUPO'] 
        
    def table_foreing_key(self):
        return {}
    
    def columns_not_null_get(self):
        return ['CODGRUPO', 'NOME', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO']

    def columns_get(self):
        return ['TEMPODEHISTORICO', 'TEMPOREPOSICAO', 'PERCENTUALSEGURANCA', 'DATASINC'] 