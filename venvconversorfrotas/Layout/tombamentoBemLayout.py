from Validations.validationData import ValidationData
class TombamentoBemLayout:         
    def table_name(self):
        return 'SCP55_TOMBAMENTOBEM'    
    def id_table_get(self):
        return ['IDBEM']
    
    def table_constraint(self):
        return ['IDBEM'] 
        
    def table_foreing_key(self):
        return {'SCP55_BEM': ['IDBEM']}
    
    def columns_not_null_get(self):
        return ['IDBEM', 'DATA', 'CODTOMBAMENTO', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO']

    def columns_get(self):
        return [] 