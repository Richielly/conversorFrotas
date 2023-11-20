import logging
from Core import imports
from Layout import saldoAnteriorBemLayout
from LayoutData import saldoAnteriorBemLayoutData, bemLayoutData, scp55_ContaContabilLayoutData
from Validations import validationData

_entity_saldoanteriorbem = saldoAnteriorBemLayout.SaldoAnteriorBemLayout()
_entity_saldoanteriorbem_data = saldoAnteriorBemLayoutData.SaldoAnteriorBemLayoutData()
_entity = _entity_saldoanteriorbem_data.entity()
_valid = validationData.ValidationData()

_bem_data = bemLayoutData.BemLayoutData()
_contaContabil_data = scp55_ContaContabilLayoutData.Scp55_ContaContabilLayoutData()

utl = imports.util
msg = imports.messages
log = imports.log
type = imports.typeConverter
file = imports.file

#Calculados
_codEntidade_CC = None
_exercicio_CC = None
_codEntidade_Bem = None
_codBem =  None
_codContaContabil =  None
_codCCReduzido =  None

class SaldoAnteriorBemLayoutReader:

    def saldoanteriorbem_reader(self,_column):
        global _entity
        global _codEntidade_CC
        global _exercicio_CC
        global _codEntidade_Bem
        global _codBem
        global _codContaContabil
        global _codCCReduzido

        _entity = dict.fromkeys(_entity, None)

        _entity['CODENTIDADE']=type.to_integer(_column[0]) #obrigatorio
        _entity['EXERCICIO']=type.to_integer(_column[1]) #obrigatorio
        _codEntidade_Bem=type.to_integer(_column[2]) #obrigatorio
        _codBem=type.to_string(_column[3]) #obrigatorio
        _codEntidade_CC=type.to_integer(_column[4]) #obrigatorio
        _exercicio_CC=type.to_integer(_column[5]) #obrigatorio
        _codContaContabil=type.to_string(_column[6]) #obrigatorio
        # _codCCReduzido=type.to_integer(_column[7]) #obrigatorio
        _entity['TIPONATUREZASALDO']=type.to_string(_column[7]) #obrigatorio
        _entity['SALDO']=type.to_float(_column[8]) #obrigatorio
        
        return _entity

    def check(self, linha):
        if _entity_saldoanteriorbem_data.exist(_entity['CODENTIDADE'], _entity['EXERCICIO'], _codEntidade_Bem, _codBem, _codEntidade_CC, _exercicio_CC, _codContaContabil):
            log.log(linha, f"O Saldo anterior do Bem {_codBem} entidade {_codEntidade_Bem} na conta contabíl {_codContaContabil} já esta gravado.", _entity_saldoanteriorbem.table_name())
            return False
        return True
    
    def valid(self, linha):
        if not _bem_data.exist(_codEntidade_Bem, _codBem)['IDBEM']:
            log.log(linha,msg=f"O Bem {_codBem} entidade {_codEntidade_Bem} não existe.",filename=_entity_saldoanteriorbem.table_name())
            return False
        if not _contaContabil_data.exist(_codEntidade_CC, _exercicio_CC, _codContaContabil):
            log.log(linha, msg=f"A conta contabil {_codContaContabil} entidade {_codEntidade_CC} exercício {_exercicio_CC} não existe.",filename=_entity_saldoanteriorbem.table_name())
            return False
        return True
        
    def save(self):
        _entity['IDSALDOANTERIORBEM'] = _valid.last_id(_entity_saldoanteriorbem.table_name())
        _entity['IDBEM']=_bem_data.exist(_codEntidade_Bem, _codBem)['IDBEM']#obrigatorio
        _entity['IDCONTACONTABIL']=_contaContabil_data.exist(_codEntidade_CC, _exercicio_CC, _codContaContabil)['IDCONTACONTABIL'] #obrigatorio
        if _entity_saldoanteriorbem_data.insert_data(_entity):
            return True
        
    def run(self, line_data, linha):
        self.saldoanteriorbem_reader(line_data)
        if self.check(linha) and self.valid(linha):
            return self.save()