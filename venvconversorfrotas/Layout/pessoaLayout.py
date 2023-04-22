from Validations.validationData import ValidationData
class PessoaLayout:         
    def table_name(self):
        return 'PESSOA'    
    def id_name_get(self):
        id_name = ValidationData()
        table = PessoaLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = PessoaLayout()
        id = id_bem.id_name_get()
        return ['CODPESSOA', 'NOME', 'CODTIPOPESSOA', 'DIGITO', 'ISUSUARIONFSE']

    def columns_get(self):
        return ['ENDERECO', 'NUMERO', 'COMPLEMENTO', 'CIDADE', 'UF', 'CEP', 'EMAIL', 'TELEFONE', 'FAX', 'CELULAR', 'CODCARGO', 'CODENTIDADEORIGEM', 'CODPESSOAORIGEM', 'ENDERECOWEB', 'CODPESSOA_CONVERSAO', 'OLD_CODPESSOAINTEGRACAO', 'BAIRRO_OLD', 'BAIRRO', 'DATASINC', 'DSOBSERVACOES', 'EHESTRANGEIRO', 'DOCESTRANGEIRO'] 