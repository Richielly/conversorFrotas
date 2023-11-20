from Validations.validationData import ValidationData
class SaldoAnteriorBemLayout:         
    def table_name(self):
        return 'SCP55_SALDOANTERIORBEM'    
    def id_table_get(self):
        return ['IDSALDOANTERIORBEM']
    
    def table_constraint(self):
        return ['CODENTIDADE', 'EXERCICIO', 'IDBEM', 'IDCONTACONTABIL'] 
        
    def table_foreing_key(self):
        return {'EXERCICIO': ['CODENTIDADE', 'EXERCICIO'], 'SCP55_BEM': ['IDBEM'], 'SCP55_CONTACONTABIL': ['IDCONTACONTABIL'], 'SCP55_TCEPR_TIPONATUREZASALDO': ['TIPONATUREZASALDO']}
    
    def columns_not_null_get(self):
        return ['IDSALDOANTERIORBEM', 'CODENTIDADE', 'EXERCICIO', 'IDBEM', 'IDCONTACONTABIL', 'TIPONATUREZASALDO', 'SALDO', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO']

    def columns_get(self):
        return [] 