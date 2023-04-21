from Validations.validationData import ValidationData
class AcumuladorLayout:         
    def table_name(self):
        return 'SCF_VEICULOACUMULADOR'    
    def id_name_get(self):
        id_name = ValidationData()
        table = AcumuladorLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDVEICULO', 'DTLEITURAACUMULADOR'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = AcumuladorLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULOABASTECIMENTO', 'IDPRODUTO', 'IDVEICULO', 'DTABASTECIMENTO', 'NRLITROSABASTECIMENTO', 'TPABASTECIMENTO', 'VLABASTECIMENTO', 'IDMOTORISTA', 'VLUNITARIO', 'ISACUMULADORFUNCIONANDO', 'NRABASTECIMENTO', 'IDVEICULOACUMULADOR', 'IDVEICULO', 'DTLEITURAACUMULADOR', 'TPORIGEMLEITURAACUMULADOR', 'VLACUMULADOR']

    def columns_get(self):
        return ['NRNOTAFISCAL', 'CODFORNECEDOR', 'DSOBSERVACAO', 'NRINTERNO', 'IDSALMOVIMENTO', 'IDREQUESICAOCOMPRAITEM', 'CODPESSOA', 'CODLOCAL', 'CODENTIDADE', 'IDENTQUANTANTESLIQREQEMP', 'IDEMPENHO', 'IDLIQUIDACAO', 'IDVEICULOABASTECIMENTO', 'TMPVLACUMULADOR'] 