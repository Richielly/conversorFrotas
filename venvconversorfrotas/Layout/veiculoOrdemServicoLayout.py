from Validations.validationData import ValidationData
class VeiculoOrdemServicoLayout:         
    def table_name(self):
        return 'SCF_VEICULOORDEMSERVICO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoOrdemServicoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'NRORDEMSERVICO'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoOrdemServicoLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULOORDEMSERVICO', 'CODENTIDADE', 'NRORDEMSERVICO', 'IDVEICULO', 'IDTIPOSERVICO', 'DTORDEMSERVICO', 'ISACUMULADORFUNCIONANDO']

    def columns_get(self):
        return ['CODFORNECEDOR', 'DTINICIOORDEMSERVICO', 'IDVEICULOACUMULADOROSINICIO', 'IDVEICULOACUMULADOROSTERMINO', 'DTTERMINOORDEMSERVICO', 'DSOBSERVACAOORDEMSERVICO', 'IDMOTORISTA', 'CODPESSOA', 'NRDIASGARANTIA', 'LOCALRESPONSAVEL', 'ORGAORESPONSAVEL', 'UNIDADERESPONSAVEL', 'CODLOCAL'] 