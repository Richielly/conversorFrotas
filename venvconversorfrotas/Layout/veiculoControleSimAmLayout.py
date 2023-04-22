from Validations.validationData import ValidationData
class VeiculoControleSimAmLayout:         
    def table_name(self):
        return 'SCF_VEICULOCONTROLESIMAM'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoControleSimAmLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDVEICULO', 'CDCONTROLE'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoControleSimAmLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULOCONTROLESIMAM', 'IDVEICULO', 'CDCONTROLE', 'CDTIPOLANCAMENTO', 'DTLANCAMENTO', 'VLRDECLARADO', 'ISTROCAACUMULADOR', 'VLRACUMULADORINICIAL', 'VLRACUMULADORFINAL', 'NOVOVALORACUMULADORINICIAL']

    def columns_get(self):
        return ['DSNOTAEXPLICATIVA', 'CDCONTROLESIMAM', 'IDVEICULOACUMULADOR'] 