from Validations.validationData import ValidationData
class OrdemAbastecimentoLayout:         
    def table_name(self):
        return 'SCF_ORDEMABASTECIMENTO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = OrdemAbastecimentoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'NRORDEMABASTECIMENTO'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = OrdemAbastecimentoLayout()
        id = id_bem.id_name_get()
        return ['IDORDEMABASTECIMENTO', 'CODENTIDADE', 'NRORDEMABASTECIMENTO', 'IDVEICULO', 'DTORDEMABASTECIMENTO', 'TPABASTECIMENTO', 'NRLITROSORDEMABASTECIMENTO', 'CODTIPOLICITACAO']

    def columns_get(self):
        return ['CODFORNECEDOR', 'IDMOTORISTA', 'IDPRODUTO', 'IDVEICULOABASTECIMENTO', 'EXERCICIOLICITACAO', 'CODLICITACAO', 'NRSALDOLICITACAO', 'CODPESSOA', 'CODLOCAL', 'IDREQUESICAOCOMPRAITEM', 'IDVEICULOCONSUMOCOMBUSTIVEL', 'DSOBSERVACAO', 'TEMPVLACUMULADOR', 'VLACUMULADOR'] 