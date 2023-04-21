from Validations.validationData import ValidationData
class BemLayout:         
    def table_name(self):
        return 'SCP55_BEM'    
    def id_name_get(self):
        id_name = ValidationData()
        table = BemLayout().table_name()
        name = id_name.search_id_name(table)
        return str(name).strip()
    
    def table_constraint(self):
        return ['CODENTIDADE','CODBEM'] #Automatizar identificação de constraint
    
    def columns_not_null_get(self):
        id_bem = BemLayout()
        id = id_bem.id_name_get()
        return [id, 'CODENTIDADE',
                'CODBEM',
                'NOME',
                'IDTIPOPROPRIEDADEBEM',
                'IDTIPOAGRUPAMENTOBEM',
                'DTOPERACAO',
                'CODGRUPO',
                'CODSUBGRUPO',
                'CODCLASSE',
                'NUMPLAQUETA',
                'NUMSIMAM',
                'DTINCLUSAOSIMAM']

    def columns_get(self):
        return [ 'DESCRICAO',
                        'NUMEROSERIE',
                        'VIDAUTILESTIMADA',
                        'DTTERMINOGARANTIA',
                        'DTINCORPORACAO',
                        'DTDESINCORPORACAO',
                        'VALOR',
                        'EXERCICIOEMPENHO',
                        'NUMEROEMPENHO',
                        'DTEMPENHO',
                        'NUMERONOTAFISCAL',
                        'SERIENOTAFISCAL',
                        'CODLOTE',
                        'CODFORNECEDOR',
                        'IDLOTE',
                        'INSCRICAOMUNICIPAL',
                        'DTINCLUSAOBAIXASIMAM',
                        'MOTIVOBAIXA']