from time import sleep
from Core import imports
from validationData import ValidationData

from LayoutData import classeLayoutData, entidadeLayoutData
_classeDataLayout = classeLayoutData.ClasseLayoutData()
_entidadeDataLayout = entidadeLayoutData.EntidadeLayoutData()

dados_entidade = [{"CODENTIDADE": "296", "NOME": "Empresa XYZ", "CNPJ": "12345678000190", "LOGRADOURO": "Rua Principal", "NUMERO": 123, "BAIRRO": "Centro", "CODCIDADE": 1001, "CEP": "12345678", "TIPOENTIDADE": "", "CODREPRESENTANTELEGAL": 1, "CARGOREPRESENTANTELEGAL": "Diretor", "CODESFERAGOVERNO": 5, "TIPOPREVIDENCIA": 1, "COMPLEMENTO": None, "EMAIL": None, "TELEFONE": None, "FAX": None, "CODENTIDADETCE": None, "INSCRICAOESTADUAL": None, "IMAGEMBRASAO": None, "CNAE": None, "CODFPAS": None, "CODIGOSICONFI": None, "IMAGEMMARCADAGUA": None, "IDNATUREZAJURIDICA": None},
         {"CODENTIDADE": "225", "NOME": "Empresa XYZ", "CNPJ": "12345678000190", "LOGRADOURO": "Rua Principal", "NUMERO": 123, "BAIRRO": "centra", "CODCIDADE": "1001", "CEP": "12345678", "TIPOENTIDADE": 1, "CODREPRESENTANTELEGAL": 1, "CARGOREPRESENTANTELEGAL": "Diretor", "CODESFERAGOVERNO": 5, "TIPOPREVIDENCIA": 1, "COMPLEMENTO": None, "EMAIL": None, "TELEFONE": None, "FAX": None, "CODENTIDADETCE": None, "INSCRICAOESTADUAL": None, "IMAGEMBRASAO": None, "CNAE": None, "CODFPAS": None, "CODIGOSICONFI": None, "IMAGEMMARCADAGUA": None, "IDNATUREZAJURIDICA": None},
         {"CODENTIDADE": 228, "NOME": "Empresa XYZ", "CNPJ": 12345678000190, "LOGRADOURO": "Rua Principal", "NUMERO": 123, "BAIRRO": "Centro", "CODCIDADE": 1001, "CEP": "12345678", "TIPOENTIDADE": 1, "CODREPRESENTANTELEGAL": 1, "CARGOREPRESENTANTELEGAL": "Diretor", "CODESFERAGOVERNO": 5, "TIPOPREVIDENCIA": 1, "COMPLEMENTO": None, "EMAIL": None, "TELEFONE": None, "FAX": None, "CODENTIDADETCE": None, "INSCRICAOESTADUAL": None, "IMAGEMBRASAO": None, "CNAE": None, "CODFPAS": None, "CODIGOSICONFI": None, "IMAGEMMARCADAGUA": None, "IDNATUREZAJURIDICA": None},
         {"CODENTIDADE": 229, "NOME": "Empresa XYZ", "CNPJ": "12345678000190", "LOGRADOURO": "Rua Principal", "NUMERO": 123, "BAIRRO": "CentroCentrado na marginal tiete para a rua generoso marques da silva sauro amadeu de alegar carvalho da costa", "CODCIDADE": 1001, "CEP": "12345678", "TIPOENTIDADE": 1, "CODREPRESENTANTELEGAL": 1, "CARGOREPRESENTANTELEGAL": "Diretor", "CODESFERAGOVERNO": 5, "TIPOPREVIDENCIA": 1, "COMPLEMENTO": None, "EMAIL": None, "TELEFONE": None, "FAX": None, "CODENTIDADETCE": None, "INSCRICAOESTADUAL": None, "IMAGEMBRASAO": None, "CNAE": None, "CODFPAS": None, "CODIGOSICONFI": None, "IMAGEMMARCADAGUA": None, "IDNATUREZAJURIDICA": None}]

for insert in dados_entidade:
    _entidadeDataLayout.insert_data(insert)
    # sleep(5)


# entidade = _classeDataLayout.entity()
# for ent in entidade:
#     if not ent[6]:
#         print(ent[0])

data_classe = [{'CODGRUPO': '99','CODSUBGRUPO': '9999', 'CODCLASSE': '111', 'NOME': 'Product Name', 'IDDERIVACAOPRODUTO': '1'},
               {'CODGRUPO': '1','CODSUBGRUPO': '11', 'CODCLASSE': '1', 'NOME': 'Product Name', 'IDDERIVACAOPRODUTO': '1'},
               {'CODGRUPO': '4','CODSUBGRUPO': '99', 'CODCLASSE': '13', 'NOME': 'Product Name', 'IDDERIVACAOPRODUTO': '1'},
               {'CODGRUPO': '2','CODSUBGRUPO': '2', 'CODCLASSE': '2', 'NOME': 'Product Name', 'IDDERIVACAOPRODUTO': '1'}]

for insert in data_classe:
    _classeDataLayout.insert_data(insert)
    # sleep(5)

