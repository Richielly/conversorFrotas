from Validations.validationData import ValidationData
class MotoristaCategoriaCnhLayout:         
    def table_name(self):
        return 'SCF_MOTORISTACATCNH'    
    def id_name_get(self):
        id_name = ValidationData()
        table = MotoristaCategoriaCnhLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['IDMOTORISTA', 'IDCATEGORIACNH'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = MotoristaCategoriaCnhLayout()
        id = id_bem.id_name_get()
        return ['IDPARAMETERSYSTEM', 'NMPARAMETERSYSTEM', 'CODENTIDADE', 'IDMARCA', 'NMMARCA', 'IDESPECIE', 'NMESPECIE', 'IDMODELO', 'IDMARCA', 'NMMODELO', 'IDESPECIE', 'IDTIPOSERVICO', 'NMTIPOSERVICO', 'TPAGENDAMENTOSERVICO', 'CODPESSOA', 'NOME', 'CODTIPOPESSOA', 'DIGITO', 'ISUSUARIONFSE', 'IDMOTORISTA', 'CODENTIDADE', 'NRCODIGOMOTORISTA', 'IDMOTORISTACATCNH', 'IDMOTORISTA', 'IDCATEGORIACNH']

    def columns_get(self):
        return ['VLPARAMETERSYSTEM', 'TPESPECIEACUMULADOR', 'IDCATEGORIACNH', 'TPVEICULOTCE', 'TPNATUREZABENS', 'TPCOMBUSTIVELTCE', 'ENDERECO', 'NUMERO', 'COMPLEMENTO', 'CIDADE', 'UF', 'CEP', 'EMAIL', 'TELEFONE', 'FAX', 'CELULAR', 'CODCARGO', 'CODENTIDADEORIGEM', 'CODPESSOAORIGEM', 'ENDERECOWEB', 'CODPESSOA_CONVERSAO', 'OLD_CODPESSOAINTEGRACAO', 'BAIRRO_OLD', 'BAIRRO', 'DATASINC', 'DSOBSERVACOES', 'EHESTRANGEIRO', 'DOCESTRANGEIRO', 'IDSERVIDOR', 'NRREGISTROCNH', 'DTPRIMEIRACNH', 'DTVALIDADECNH', 'TPMODELOCNH', 'DTEMISSAOCNH', 'CODPESSOAFISICA', 'ATIVO'] 