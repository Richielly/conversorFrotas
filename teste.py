import pandas as pd
from datetime import timedelta
from io import StringIO

# Exemplo de dados CSV
data = '''order_id,device_id,order_creation_time,poll_preceding_order,poll_following_order,last_conn_time,last_conn_status
1,101,2023-04-23 10:00:00,2023-04-23 09:59:55,2023-04-23 10:00:05,2023-04-23 09:59:50,200
2,102,2023-04-23 11:00:00,2023-04-23 10:59:55,2023-04-23 11:00:05,2023-04-23 10:59:50,401
3,103,2023-04-23 12:00:00,2023-04-23 11:59:55,2023-04-23 12:00:05,2023-04-23 11:59:50,0
'''

# Lendo o arquivo CSV a partir de uma string (substituir esta linha para ler de um arquivo real)
df = pd.read_csv(StringIO(data), parse_dates=["order_creation_time", "poll_preceding_order", "poll_following_order", "last_conn_time"])

# Inicializando colunas adicionais
additional_columns = [
    "total_count_3min_prior", "status_0_3min_prior", "status_200_3min_prior", "status_401_3min_prior", "error_econnaborted_3min_prior", "error_generic_error_3min_prior", "error_none_3min_prior",
    "total_count_3min_after", "status_0_3min_after", "status_200_3min_after", "status_401_3min_after", "error_econnaborted_3min_after", "error_generic_error_3min_after", "error_none_3min_after",
    "total_count_60min_prior", "status_0_60min_prior", "status_200_60min_prior", "status_401_60min_prior", "error_econnaborted_60min_prior", "error_generic_error_60min_prior", "error_none_60min_prior"
]

for col in additional_columns:
    df[col] = 0

# Atualize as funções e o loop 'for' de acordo com os dados fornecidos e os requisitos específicos mencionados nas instruções iniciais. Isso inclui ajustar os nomes das colunas, tipos de erros e códigos de status conforme necessário.

# Salvando o resultado em um novo arquivo CSV
df.to_csv("output_data.csv", index=False)
