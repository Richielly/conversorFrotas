from Validations.validationData import ValidationData as valid
from Layout import bemLayout
v = valid()
bem = bemLayout.BemLayout()
table = bem.table_name()
colunas = bem.columns_not_null_get()
id = v.last_id('SCP55_BEM')

if (v.exist(table, ['53', '99'], bem.table_constraint()) != None):
    print('Pode gravar')

else:
    print(f'Este registro entidade ... bem ... já esta gravado.')
# values = [id, '053',
#                 '999999',
#                 'teste',
#                 '1',
#                 '1',
#                 '19.02.2023',
#                 '99',
#                 '9999',
#                 '9999',
#                 '99999999',
#                 '99999999',
#                 '19.02.2023']
#
#
# print(v.insert_data(table, colunas,values))

