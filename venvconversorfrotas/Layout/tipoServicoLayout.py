from Validations.validationData import ValidationData
class TipoServicoLayout:         
    def table_name(self):
        return 'SCF_TIPOSERVICO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = TipoServicoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['NMTIPOSERVICO'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = TipoServicoLayout()
        id = id_bem.id_name_get()
        return ['IDTIPOSERVICO', 'NMTIPOSERVICO', 'TPAGENDAMENTOSERVICO']

    def columns_get(self):
        return [] 