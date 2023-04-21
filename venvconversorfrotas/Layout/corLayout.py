from Validations.validationData import ValidationData
class CorLayout:         
    def table_name(self):
        return 'COR'    
    def id_name_get(self):
        id_name = ValidationData()
        table = CorLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['NMCOR'] #Automatizar identifica��o de constraint
    
    def columns_not_null_get(self):
        id_bem = CorLayout()
        id = id_bem.id_name_get()
        return ['IDCOR', 'NMCOR']

    def columns_get(self):
        return [] 