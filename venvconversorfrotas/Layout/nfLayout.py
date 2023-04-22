from Validations.validationData import ValidationData
class NfLayout:         
    def table_name(self):
        return 'SCF_NF'    
    def id_name_get(self):
        id_name = ValidationData()
        table = NfLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODFORNECEDOR', 'IDTIPODOCFISCAL', 'IDTIPOSERIEDOCFISCAL', 'NUMERONOTAABASTECIMENTO', 'IDNF'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = NfLayout()
        id = id_bem.id_name_get()
        return ['IDNF', 'CODFORNECEDOR', 'IDTIPODOCFISCAL', 'IDTIPOSERIEDOCFISCAL', 'NUMERONOTAABASTECIMENTO']

    def columns_get(self):
        return ['DATAEMISSAO', 'VALORNOTAFISCAL', 'PERMITEAJUSTEDEVALORES', 'DATAINICIOFATURAMENTO', 'DATAFINALFATURAMENTO', 'STATUSNFABASTECIMENTO', 'PROCESSADO', 'CODENTIDADE', 'VALORNOTAFISCALCALCULADO'] 