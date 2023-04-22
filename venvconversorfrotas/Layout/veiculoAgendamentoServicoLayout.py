from Validations.validationData import ValidationData
class VeiculoAgendamentoServicoLayout:         
    def table_name(self):
        return 'SCF_VEICULOAGENDAMENTOSERVIC'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoAgendamentoServicoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identifica��o de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoAgendamentoServicoLayout()
        id = id_bem.id_name_get()
        return []

    def columns_get(self):
        return [] 