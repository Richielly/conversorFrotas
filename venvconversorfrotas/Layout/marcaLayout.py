from Validations.validationData import ValidationData
class MarcaLayout:         
    def table_name(self):
        return 'MARCA'    
    def id_name_get(self):
        id_name = ValidationData()
        table = MarcaLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = MarcaLayout()
        id = id_bem.id_name_get()
        return ['IDPARAMETERSYSTEM', 'NMPARAMETERSYSTEM', 'CODENTIDADE', 'IDMARCA', 'NMMARCA']

    def columns_get(self):
        return ['VLPARAMETERSYSTEM'] 