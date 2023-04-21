from Validations.validationData import ValidationData
class EspecieLayout:         
    def table_name(self):
        return 'SCF_ESPECIE'    
    def id_name_get(self):
        id_name = ValidationData()
        table = EspecieLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = EspecieLayout()
        id = id_bem.id_name_get()
        return ['IDPARAMETERSYSTEM', 'NMPARAMETERSYSTEM', 'CODENTIDADE', 'IDMARCA', 'NMMARCA', 'IDESPECIE', 'NMESPECIE']

    def columns_get(self):
        return ['VLPARAMETERSYSTEM', 'TPESPECIEACUMULADOR', 'IDCATEGORIACNH', 'TPVEICULOTCE', 'TPNATUREZABENS'] 