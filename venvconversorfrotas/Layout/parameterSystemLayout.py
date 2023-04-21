from Validations.validationData import ValidationData
class ParameterSystemLayout:         
    def table_name(self):
        return 'SCF_PARAMETERSYSTEM'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ParameterSystemLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'NMPARAMETERSYSTEM'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ParameterSystemLayout()
        id = id_bem.id_name_get()
        return ['IDPARAMETERSYSTEM', 'NMPARAMETERSYSTEM', 'CODENTIDADE']

    def columns_get(self):
        return ['VLPARAMETERSYSTEM'] 