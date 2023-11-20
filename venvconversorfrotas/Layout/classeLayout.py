from Validations.validationData import ValidationData
class ClasseLayout:         
    def table_name(self):
        return 'CLASSE'    
    def id_table_get(self):
        return ['CODGRUPO', 'CODSUBGRUPO', 'CODCLASSE']
    
    def table_constraint(self):
        return ['CODGRUPO', 'CODSUBGRUPO', 'CODCLASSE'] 
        
    def table_foreing_key(self):
        return {'CLASSEFAMILIA': ['CODCLASSEFAMILIA'], 'SAL_DERIVACAOPRODUTO': ['IDDERIVACAOPRODUTO'], 'SUBGRUPO': ['CODSUBGRUPO', 'CODGRUPO']}
    
    def columns_not_null_get(self):
        return ['CODGRUPO', 'CODSUBGRUPO', 'CODCLASSE', 'NOME', 'IDDERIVACAOPRODUTO', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO']

    def columns_get(self):
        return ['CODCLASSEFAMILIA', 'TEMPODEHISTORICO', 'TEMPOREPOSICAO', 'PERCENTUALSEGURANCA', 'DATASINC'] 