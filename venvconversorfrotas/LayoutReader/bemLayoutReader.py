import logging

from Layout import scp55_TcePR_TipoAgrupamentoBemLayout
from Core import imports
from Layout import bemLayout
from LayoutData import bemLayoutData, scp55_TcePR_TipoAgrupamentoBemLayoutData, fornecedorLayoutData, grupoLayoutData, subGrupoLayoutData, classeLayoutData, pessoaJuridicaLayoutData
from Validations import validationData

_entity_bem = bemLayout.BemLayout()
_entity_bem_data = bemLayoutData.BemLayoutData()
_entity = _entity_bem_data.entity()

_entity_scp55_TcePR_TipoAgrupamentoBem = scp55_TcePR_TipoAgrupamentoBemLayout.Scp55_TcePR_TipoAgrupamentoBemLayout()
_entity_scp55_TcePR_TipoAgrupamentoBem_data = scp55_TcePR_TipoAgrupamentoBemLayoutData.Scp55_TcePR_TipoAgrupamentoBemLayoutData()

_entity_grupo_data = grupoLayoutData.GrupoLayoutData()
_entity_subGrupo_data = subGrupoLayoutData.SubGrupoLayoutData()
_entity_classe_data = classeLayoutData.ClasseLayoutData()
_entity_fornecedor_data = fornecedorLayoutData.FornecedorLayoutData()
_entity_pessoa_juridica_data = pessoaJuridicaLayoutData.PessoaJuridicaLayoutData()

_valid = validationData.ValidationData()

utl = imports.util
msg = imports.messages
log = imports.log
type = imports.typeConverter
file = imports.file

#Calculados
_idtiponaturezabem=None
_idtipocategoriabem=None
_idtpdetalhamentobem=None
_idtipoutilizacaobem=None
_nomeGrupo = None
_nomeSubGrupo = None
_nomeClasse = None
_cnpj = None

class BemLayoutReader:

    def bem_reader(self,_column):
        global _entity

        global _idtiponaturezabem
        global _idtipocategoriabem
        global _idtpdetalhamentobem
        global _idtipoutilizacaobem
        global _nomeGrupo
        global _nomeSubGrupo
        global _nomeClasse
        global _cnpj

        _entity = dict.fromkeys(_entity, None)

        _entity['CODENTIDADE']=type.to_integer(_column[0]) #obrigatorio
        _entity['CODBEM']=type.to_string(_column[1]) #obrigatorio
        _entity['NOME']=type.to_string(_column[2]) #obrigatorio
        _entity['IDTIPOPROPRIEDADEBEM']=type.to_integer(_column[3]) #obrigatorio
        _idtiponaturezabem = type.to_integer(_column[4])   # Calculados _entity['IDTIPOAGRUPAMENTOBEM'] #obrigatorio
        _idtipocategoriabem = type.to_integer(_column[5])  # Calculados _entity['IDTIPOAGRUPAMENTOBEM'] #obrigatorio
        _idtpdetalhamentobem = type.to_integer(_column[6]) # Calculados _entity['IDTIPOAGRUPAMENTOBEM'] #obrigatorio
        _idtipoutilizacaobem = type.to_integer(_column[7]) # Calculados _entity['IDTIPOAGRUPAMENTOBEM'] #obrigatorio
        _entity['DTOPERACAO']=type.string_to_date(_column[8]) #obrigatorio
        _nomeGrupo=type.to_string(_column[9]) #obrigatorio
        _nomeSubGrupo = type.to_string(_column[10])  # obrigatorio
        _nomeClasse = type.to_string(_column[11])  # obrigatorio
        _entity['NUMSIMAM']=type.to_string(_column[12]) #obrigatorio
        _entity['DTINCLUSAOSIMAM']=type.string_to_date(_column[13]) #obrigatorio
        _entity['DESCRICAO']=type.string_to_blob(_column[14])
        _entity['NUMPLAQUETA']=type.to_float(_column[15])
        _entity['NUMEROSERIE']=type.to_string(_column[16])
        _entity['VIDAUTILESTIMADA']=type.to_integer(_column[17])
        _entity['DTTERMINOGARANTIA']=type.string_to_date(_column[18])
        _entity['DTINCORPORACAO']=type.string_to_date(_column[19])
        _entity['DTDESINCORPORACAO']=type.string_to_date(_column[20])
        _entity['VALOR']=type.to_float(_column[21])
        _entity['EXERCICIOEMPENHO']=type.to_integer(_column[22])
        _entity['NUMEROEMPENHO']=type.to_integer(_column[23])
        _entity['DTEMPENHO']=type.string_to_date(_column[24])
        _entity['NUMERONOTAFISCAL']=type.to_integer(_column[25])
        _entity['SERIENOTAFISCAL']=type.to_string(_column[26])
        _entity['CODLOTE']=type.to_integer(_column[27])
        _cnpj=type.to_string(_column[28])
        _entity['IDLOTE']=type.to_integer(_column[29])
        _entity['INSCRICAOMUNICIPAL']=type.to_string(_column[30])
        _entity['DTINCLUSAOBAIXASIMAM']=type.string_to_date(_column[31])
        _entity['MOTIVOBAIXA']=type.to_string(_column[32])
        
        return _entity
      
    def check(self, linha):
        if _entity_bem_data.exist(_entity['CODENTIDADE'], _entity['CODBEM']):
            log.log(linha, f"O Bem {_entity['CODBEM']} entidade {_entity['CODENTIDADE']} já esta gravado.", _entity_bem.table_name())
            return False
        if not _entity_scp55_TcePR_TipoAgrupamentoBem_data.exist(_idtiponaturezabem, _idtipocategoriabem, _idtpdetalhamentobem, _idtipoutilizacaobem):
            log.log(linha, f"O tipo agrupamento bem tce com tipo natureza {_idtiponaturezabem} tipo categoria {_idtipocategoriabem} detalhamento {_idtpdetalhamentobem} tipo de utilização {_idtipoutilizacaobem} que esta sendo usado para o Bem da entidade {_entity['CODENTIDADE']} código {_entity['CODBEM']} não existe.",_entity_bem.table_name())
            return False
        return True

    def valid(self, linha):
        if not utl.valid_size(_entity['NOME'], 81):
            log.log(linha, f"O nome do bem {_entity['CODBEM']} entidade {_entity['CODENTIDADE']} deve ter entre 1 e 80 caracteres e esta com tamanho {len(_entity['NOME'])}.", _entity_bem.table_name())
            return False

        if not _entity_pessoa_juridica_data.exist(_entity['CNPJ']):
            log.log(linha, f"O fornecedor cnpj {_entity['CNPJ']} não existe.", _entity_bem.table_name())
            return False
        else:
            _entity['CODFORNECEDOR'] = _entity_pessoa_juridica_data.exist(_cnpj)['CODPESSOA']

        if not _entity_fornecedor_data.exist(_entity['CODFORNECEDOR']):
            log.log(linha, f"O fornecedor código {_entity['CODFORNECEDOR']} não existe.", _entity_bem.table_name())
            return False
        
        if not _entity_grupo_data.exist(_nomeGrupo):
            log.log(linha, f"O grupo {_nomeGrupo} não existe.", _entity_bem.table_name())
            return False
        else:
            _entity['CODGRUPO'] = _entity_grupo_data.exist(_nomeGrupo)['CODGRUPO']
            
        if not _entity_subGrupo_data.exist(_entity['CODGRUPO'], _nomeSubGrupo):
            log.log(linha, f"O subgrupo {_nomeSubGrupo} não existe.", _entity_bem.table_name())
            return False
        else:
            _entity['CODSUBGRUPO'] = _entity_subGrupo_data.exist(_entity['CODGRUPO'], _nomeSubGrupo)['CODSUBGRUPO']
        
        if not _entity_classe_data.exist(_entity['CODGRUPO'], _entity['CODSUBGRUPO'], _nomeClasse):
            log.log(linha, f"A classe {_nomeClasse} não existe.", _entity_bem.table_name())
            return False
        else:
            _entity['CODCLASSE'] = _entity_classe_data.exist(_entity['CODGRUPO'], _entity['CODSUBGRUPO'], _nomeClasse)['CODCLASSE']
        return True
        
    def save(self):
        _entity['IDBEM'] = _valid.last_id(_entity_bem.table_name())
        _entity['IDTIPOAGRUPAMENTOBEM']=_entity_scp55_TcePR_TipoAgrupamentoBem_data.exist(_idtiponaturezabem, _idtipocategoriabem, _idtpdetalhamentobem, _idtipoutilizacaobem)['IDTIPOAGRUPAMENTOBEM']

        if _entity_bem_data.insert_data(_entity):
            return True
        else:False
               
    def run(self, line_data, linha):
        self.bem_reader(line_data)
        if self.check(linha) and self.valid(linha):
            return self.save()
