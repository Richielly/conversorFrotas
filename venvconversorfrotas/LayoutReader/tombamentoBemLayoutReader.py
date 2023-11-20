import logging
from Core import imports
from Layout import tombamentoBemLayout
from LayoutData import tombamentoBemLayoutData, bemLayoutData
from Validations import validationData

_entity_tombamentobem = tombamentoBemLayout.TombamentoBemLayout()
_entity_tombamentobem_data = tombamentoBemLayoutData.TombamentoBemLayoutData()
_entity = _entity_tombamentobem_data.entity()
_valid = validationData.ValidationData()

_bem = bemLayoutData.BemLayoutData()

utl = imports.util
msg = imports.messages
log = imports.log
type = imports.typeConverter
file = imports.file

#Calculados
_codEntidade = None
_codBem = None

class TombamentoBemLayoutReader:

    def tombamentobem_reader(self,_column):
        global _entity
        global _codEntidade
        global _codBem

        _entity = dict.fromkeys(_entity, None)

        _codEntidade = _column[0]   #IDBEM #obrigatorio
        _codBem = _column[1]    #IDBEM #obrigatorio
        _entity['DATA']=type.string_to_date(_column[2]) #obrigatorio
        _entity['CODTOMBAMENTO']=type.to_string(_column[3]) #obrigatorio
        
        return _entity
      
    def check(self, linha):
        if _entity_tombamentobem_data.exist(_codEntidade, _codBem):
            log.log(linha, f"O Tombamento do Bem código {_codBem} entidade {_codEntidade} já esta gravado.", _entity_tombamentobem.table_name())
            return False
        return True
    
    def valid(self, linha):
        if not _bem.exist(_codEntidade, _codBem):
            log.log(linha, f"O Bem {_codBem} entidade {_codEntidade} não existe.", _entity_tombamentobem.table_name())
            return False
        return True
    def save(self):
        _entity['IDBEM'] = _bem.exist(_codEntidade, _codBem)['IDBEM']
        if _entity_tombamentobem_data.insert_data(_entity):
            return True

    def run(self, line_data, linha):
        self.tombamentobem_reader(line_data)
        if self.check(linha) and self.valid(linha):
            return self.save()