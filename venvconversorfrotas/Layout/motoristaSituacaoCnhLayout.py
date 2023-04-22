from Validations.validationData import ValidationData
class MotoristaSituacaoCnhLayout:         
    def table_name(self):
        return 'SCF_MOTORISTASITUACAOCNH'    
    def id_name_get(self):
        id_name = ValidationData()
        table = MotoristaSituacaoCnhLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDMOTORISTA', 'DTSITUACAOCNH'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = MotoristaSituacaoCnhLayout()
        id = id_bem.id_name_get()
        return ['IDMOTORISTASITUACAOCNH', 'IDMOTORISTA', 'DTSITUACAOCNH', 'IDSITUACAOCNH', 'NRPONTOSVIGENTES']

    def columns_get(self):
        return [] 