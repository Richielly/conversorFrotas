from Validations.validationData import ValidationData
class VeiculoLayout:         
    def table_name(self):
        return 'SCF_VEICULO'    
    def id_name_get(self):
        id_name = ValidationData()
        table = VeiculoLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE', 'IDBEMOBRIGACAO', 'IDBEM', 'CODENTIDADE', 'NRFROTA'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = VeiculoLayout()
        id = id_bem.id_name_get()
        return ['IDVEICULO', 'IDMODELO', 'IDCOR', 'NRPASSAGEIRO', 'ISACUMULADORFUNCIONANDO', 'DTINCLUSAOSIMAM', 'NRCILINDRADAS', 'NRPOTENCIAMOTOR', 'NRCAPACIDADETANQUECOMB', 'NRCAPACIDADECARGA']

    def columns_get(self):
        return ['CODENTIDADE', 'IDBEMOBRIGACAO', 'NRFROTA', 'NRPLACA', 'NRRENAVAM', 'NRCHASSI', 'NRMOTOR', 'NRANOFABRICACAO', 'NRANOMODELO', 'NRCILINDRADAS_OLD', 'NRPOTENCIAMOTOR_OLD', 'NRCAPACIDADETANQUECOMB_OLD', 'NRCAPACIDADECARGA_OLD', 'DSOBSERVACAO', 'TPVINCULO', 'IDFIPEMODELO', 'TPCOMBUSTIVEL', 'IDBEM', 'IDTPCATEGOBJETODESP', 'IDTPOBJETODESP', 'IMPRESSAODIARIOBORDO', 'MEDIACONSUMO'] 