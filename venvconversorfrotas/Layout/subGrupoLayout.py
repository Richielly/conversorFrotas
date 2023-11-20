from Validations.validationData import ValidationData
class SubGrupoLayout:         
    def table_name(self):
        return 'SUBGRUPO'    
    def id_table_get(self):
        return ['CODGRUPO', 'CODSUBGRUPO']
    
    def table_constraint(self):
        return ['CODGRUPO', 'CODSUBGRUPO'] 
        
    def table_foreing_key(self):
        return {'GRUPO': ['CODGRUPO']}
    
    def columns_not_null_get(self):
        return ['CODGRUPO', 'CODSUBGRUPO', 'NOME', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO']

    def columns_get(self):
        return ['TEMPODEHISTORICO', 'TEMPOREPOSICAO', 'PERCENTUALSEGURANCA', 'DATASINC'] 