from Validations.validationData import ValidationData
class MotoristaCategoriaCnhLayout:         
    def table_name(self):
        return 'SCF_MOTORISTACATCNH'    
    def id_name_get(self):
        id_name = ValidationData()
        table = MotoristaCategoriaCnhLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDMOTORISTA', 'IDCATEGORIACNH'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = MotoristaCategoriaCnhLayout()
        id = id_bem.id_name_get()
        return ['IDMOTORISTACATCNH', 'IDMOTORISTA', 'IDCATEGORIACNH']

    def columns_get(self):
        return [] 