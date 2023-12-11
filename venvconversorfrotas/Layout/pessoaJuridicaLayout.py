from Validations.validationData import ValidationData
class PessoaJuridicaLayout:         
    def table_name(self):
        return 'PESSOAJURIDICA'    
    def id_table_get(self):
        return ['CODPESSOA']
    
    def table_constraint(self):
        return ['CNPJ'] 
        
    def table_foreing_key(self):
        return {'PESSOA': ['CODPESSOA'], 'PESSOAFISICA': ['CODRESPONSAVEL']}
    
    def columns_not_null_get(self):
        return ['CODPESSOA']

    def columns_get(self):
        return ['CNPJ', 'INSCRICAOESTADUAL', 'INSCRICAOMUNICIPAL', 'CODRESPONSAVEL', 'NOMEFANTASIA', 'NOMECONTADOR', 'TELEFONECONTADOR', 'TIPOORGAO', 'OBJETOSOCIAL_OLD', 'OBJETOSOCIAL'] 