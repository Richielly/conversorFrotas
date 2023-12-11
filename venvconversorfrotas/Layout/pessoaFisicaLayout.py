from Validations.validationData import ValidationData
class PessoaFisicaLayout:         
    def table_name(self):
        return 'PESSOAFISICA'    
    def id_table_get(self):
        return ['CODPESSOA']
    
    def table_constraint(self):
        return ['CODPESSOA'] 
        
    def table_foreing_key(self):
        return {'CBO_OCUPACAO': ['IDOCUPACAO'], 'ESTADOCIVIL': ['CODESTADOCIVIL'], 'FORMACAO': ['CODFORMACAO'], 'LOG_UF': ['IDUFEMISSAOTITELEITOR'], 'PESSOA': ['CODPESSOA']}
    
    def columns_not_null_get(self):
        return ['CODPESSOA', 'TPSEXO', 'TPMODELOCNH']

    def columns_get(self):
        return ['CPF', 'RG', 'DATANASCIMENTO', 'CODESTADOCIVIL', 'CODFORMACAO', 'CODCONTRIBUINTEINDIVIDUALINSS', 'CODCBO', 'IDOCUPACAO', 'DSRGEMISSOR', 'DSRGUF', 'DTEMISSAORG', 'NRTITULOELEITORZONA', 'NRTITULOELEITORSECAO', 'NRTITULOELEITOR', 'NRTITULOELEITORDIGITO', 'NRREGISTROCNH', 'DTPRIMEIRACNH', 'DTEMISSAOCNH', 'DTVALIDADECNH', 'NUMERORIC', 'DTEXPEDICAORIC', 'DTVALIDADERIC', 'CERTIFICADORESERVISTA', 'DTEMISSAOTITELEITOR', 'IDUFEMISSAOTITELEITOR'] 