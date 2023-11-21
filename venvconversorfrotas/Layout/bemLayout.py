from Validations.validationData import ValidationData
class BemLayout:         
    def table_name(self):
        return 'SCP55_BEM'    
    def id_table_get(self):
        return ['IDBEM']
    
    def table_constraint(self):
        return ['CODENTIDADE', 'CODBEM'] 
        
    def table_foreing_key(self):
        return {'CLASSE': ['CODCLASSE', 'CODSUBGRUPO', 'CODGRUPO'], 'ENTIDADE': ['CODENTIDADE'], 'FORNECEDOR': ['CODFORNECEDOR'], 'SCP55_LOTE': ['IDLOTE'], 'SCP55_TCEPR_TIPOAGRUPAMENTOBEM': ['IDTIPOAGRUPAMENTOBEM'], 'SCP55_TCEPR_TIPOPROPRIEDADEBEM': ['IDTIPOPROPRIEDADEBEM']}
    
    def columns_not_null_get(self):
        return ['IDBEM', 'CODENTIDADE', 'CODBEM', 'NOME', 'IDTIPOPROPRIEDADEBEM', 'IDTIPOAGRUPAMENTOBEM', 'DTOPERACAO', 'CODGRUPO', 'CODSUBGRUPO', 'CODCLASSE', 'NUMSIMAM', 'OPERADORCRIADOR', 'DATACRIACAO', 'OPERADORATUALIZADOR', 'DATAATUALIZACAO', 'DTINCLUSAOSIMAM']

    def columns_get(self):
        return ['DESCRICAO', 'NUMPLAQUETA', 'NUMEROSERIE', 'VIDAUTILESTIMADA', 'DTTERMINOGARANTIA', 'DTINCORPORACAO', 'DTDESINCORPORACAO', 'VALOR', 'EXERCICIOEMPENHO', 'NUMEROEMPENHO', 'DTEMPENHO', 'NUMERONOTAFISCAL', 'SERIENOTAFISCAL', 'CODLOTE', 'CODFORNECEDOR', 'IDLOTE', 'INSCRICAOMUNICIPAL', 'DTINCLUSAOBAIXASIMAM', 'MOTIVOBAIXA']
