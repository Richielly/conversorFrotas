from Validations.validationData import ValidationData
class Scp55_ContaContabilLayout:         
    def table_name(self):
        return 'SCP55_CONTACONTABIL'    
    def id_table_get(self):
        return ['IDCONTACONTABIL']
    
    def table_constraint(self):
        return ['CODENTIDADE', 'EXERCICIO', 'CODCONTACONTABIL', 'CODENTIDADE', 'EXERCICIO', 'CODCCREDUZIDO'] 
        
    def table_foreing_key(self):
        return {'EXERCICIO': ['CODENTIDADE', 'EXERCICIO'], 'SCP55_CONTACONTABIL': ['CODCCSUPERIOR', 'CODENTIDADE', 'EXERCICIO'], 'SCP55_TCEPR_TIPONATUREZASALDO': ['TIPONATUREZASALDO'], 'SCP55_TCEPR_TIPOSUPERAVITFINAN': ['TIPOSUPERAVITFINAN']}
    
    def columns_not_null_get(self):
        return ['IDCONTACONTABIL', 'CODENTIDADE', 'EXERCICIO', 'CODCONTACONTABIL', 'CODCCREDUZIDO', 'NOME', 'EHANALITICA', 'NIVEL', 'TIPONATUREZASALDO', 'TIPOSUPERAVITFINAN', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO', 'DTINCLUSAOSIMAM', 'FLAGENCERRAMENTO']

    def columns_get(self):
        return ['CODCCSUPERIOR'] 