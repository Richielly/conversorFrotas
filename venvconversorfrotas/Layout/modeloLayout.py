from Validations.validationData import ValidationData
class ModeloLayout:         
    def table_name(self):
        return 'SCF_MODELO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ModeloLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['NMMODELO', 'IDESPECIE'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ModeloLayout()
        id = id_bem.id_name_get()
        return ['IDMODELO', 'IDMARCA', 'NMMODELO', 'IDESPECIE']

    def columns_get(self):
        return ['TPCOMBUSTIVELTCE'] 