from Validations.validationData import ValidationData
class MotoristaLayout:         
    def table_name(self):
        return 'SCF_MOTORISTA'    
    def id_name_get(self):
        id_name = ValidationData()
        table = MotoristaLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'NRCODIGOMOTORISTA'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = MotoristaLayout()
        id = id_bem.id_name_get()
        return ['IDMOTORISTA', 'CODENTIDADE', 'NRCODIGOMOTORISTA']

    def columns_get(self):
        return ['IDSERVIDOR', 'NRREGISTROCNH', 'DTPRIMEIRACNH', 'DTVALIDADECNH', 'TPMODELOCNH', 'DTEMISSAOCNH', 'CODPESSOAFISICA', 'ATIVO'] 