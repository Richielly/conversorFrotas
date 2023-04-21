from Validations.validationData import ValidationData
class AbastecimentoLayout:         
    def table_name(self):
        return 'SCF_VEICULOABASTECIMENTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = AbastecimentoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return [] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = AbastecimentoLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULOABASTECIMENTO', 'IDPRODUTO', 'IDVEICULO', 'DTABASTECIMENTO', 'NRLITROSABASTECIMENTO', 'TPABASTECIMENTO', 'VLABASTECIMENTO', 'IDMOTORISTA', 'VLUNITARIO', 'ISACUMULADORFUNCIONANDO', 'NRABASTECIMENTO']

    def columns_get(self):
        return ['NRNOTAFISCAL', 'CODFORNECEDOR', 'DSOBSERVACAO', 'NRINTERNO', 'IDSALMOVIMENTO', 'IDREQUESICAOCOMPRAITEM', 'CODPESSOA', 'CODLOCAL', 'CODENTIDADE', 'IDENTQUANTANTESLIQREQEMP', 'IDEMPENHO', 'IDLIQUIDACAO'] 