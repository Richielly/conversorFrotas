from Validations.validationData import ValidationData
class ConsumoCombustivelLayout:         
    def table_name(self):
        return 'SCF_CONSUMOCOMBUSTIVEL'    
    def id_name_get(self):
        id_name = ValidationData()
        table = ConsumoCombustivelLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = ConsumoCombustivelLayout()
        id = id_bem.id_name_get()
        return ['IDCONSUMOCOMBUSTIVEL', 'CODENTIDADE', 'NRSEQUENCIAL', 'IDVEICULO', 'NRMES', 'NRANO', 'IDTIPOCATEGORIAOBJETODESPESA', 'IDTIPOOBJETODESPESA', 'NRQUANTIDADE']

    def columns_get(self):
        return [] 