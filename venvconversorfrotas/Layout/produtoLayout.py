from Validations.validationData import ValidationData
class ProdutoLayout:         
    def table_name(self):
        return 'PRODUTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ProdutoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ProdutoLayout()
        id = id_bem.id_name_get()
        return ['CODPRODUTO', 'CODGRUPO', 'CODSUBGRUPO', 'CODCLASSE', 'SIGLAESTOQUE', 'SIGLACOMPRA', 'NOME', 'PRECOMAXIMO', 'PRECOMINIMO', 'FLAGATIVO', 'PERMITIRSOLICSEMLIBERACAO', 'FLAGCONTROLAVALIDADE', 'FLAGCONTROLALOTE', 'TIPOCOMBUSTIVELSIMAM', 'FLAGEXIGEREGISTROANVISA', 'FLAGEXIGECNPJFABRICANTE']

    def columns_get(self):
        return ['ITEMID', 'IDDERIVACAOPRODUTO', 'TEMPOREPOSICAO', 'DESCRICAO', 'IDTPCATEGOBJETODESP', 'IDTPOBJETODESP', 'NOMECOMERCIAL', 'CATMAT_BPS', 'UNIDADE_BPS', 'GENERICO_BPS', 'REGISTROANVISA', 'PERCENTUALSEGURANCA', 'TEMPODEHISTORICO', 'DATASINC'] 