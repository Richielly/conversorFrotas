from Validations.validationData import ValidationData
class NfAbastecimentoLayout:         
    def table_name(self):
        return 'SCF_NFABASTECIMENTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = NfAbastecimentoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = NfAbastecimentoLayout()
        id = id_bem.id_name_get()
        return ['IDNFABASTECIMENTOVEICULO']

    def columns_get(self):
        return ['IDVEICULOABASTECIMENTO', 'VALORTOTALAJUSTADO', 'IDNF', 'VALORLITROAJUSTADO'] 