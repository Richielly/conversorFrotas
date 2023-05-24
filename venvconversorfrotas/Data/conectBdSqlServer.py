import pyodbc

# def procurar_palavra_em_tabelas(server, database, username, password, palavra_procurada):
#     conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
#     conn = pyodbc.connect(conn_str)
#     cursor = conn.cursor()
#
#     script_sql = f"""
#     DECLARE @palavraProcurada NVARCHAR(255) = '{palavra_procurada}';
#     DECLARE @tabelaNome NVARCHAR(255);
#     DECLARE @colunaNome NVARCHAR(255);
#     DECLARE @consulta NVARCHAR(MAX);
#
#     DECLARE tabelaColuna_cursor CURSOR FOR
#     SELECT t.TABLE_NAME, c.COLUMN_NAME
#     FROM INFORMATION_SCHEMA.TABLES AS t
#     JOIN INFORMATION_SCHEMA.COLUMNS AS c ON c.TABLE_NAME = t.TABLE_NAME
#     WHERE t.TABLE_TYPE = 'BASE TABLE'
#     AND c.DATA_TYPE IN ('nvarchar', 'varchar', 'text', 'ntext');
#
#     OPEN tabelaColuna_cursor;
#
#     FETCH NEXT FROM tabelaColuna_cursor INTO @tabelaNome, @colunaNome;
#
#     WHILE @@FETCH_STATUS = 0
#     BEGIN
#         SET @consulta = 'IF EXISTS (SELECT * FROM ' + QUOTENAME(@tabelaNome) + ' WHERE ' + QUOTENAME(@colunaNome) + ' LIKE ''%' + @palavraProcurada + '%'') '
#                       + 'BEGIN '
#                       + '    PRINT ''Palavra encontrada em: Tabela - ' + @tabelaNome + ', Coluna - ' + @colunaNome + '''; '
#                       + 'END';
#
#         EXEC sp_executesql @consulta;
#
#         FETCH NEXT FROM tabelaColuna_cursor INTO @tabelaNome, @colunaNome;
#     END;
#
#     CLOSE tabelaColuna_cursor;
#     DEALLOCATE tabelaColuna_cursor;
#     """
#
#     cursor.execute(script_sql)
#
#     while True:
#         row = cursor.fetchone()
#         if not row:
#             break
#         print(row[0])
#
#     cursor.close()
#     conn.close()
#
# # Exemplo de uso:
# server = 'PAT-1620\SQLEXPRESS'
# database = 'master'
# username = 'PAT-1620\Equiplano'
# password = 'es74079'
# palavra_procurada = 'gasolina'
#
# procurar_palavra_em_tabelas(server, database, username, password, palavra_procurada)

import pyodbc

def handle_messages(msg_no, msg_state, msg_severity, msg_text, msg_server, msg_proc, msg_line):
    print(f"Palavra encontrada em: Tabela - {msg_text.strip()}")

def procurar_palavra_em_tabelas(server, database, palavra_procurada):
    conn = pyodbc.connect(f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;")
    conn.add_output_converter(-155, handle_messages)
    cursor = conn.cursor()

    script_sql = f"""
    DECLARE @palavraProcurada NVARCHAR(255) = '{palavra_procurada}';
    DECLARE @tabelaNome NVARCHAR(255);
    DECLARE @colunaNome NVARCHAR(255);
    DECLARE @consulta NVARCHAR(MAX);

    DECLARE tabelaColuna_cursor CURSOR FOR
    SELECT t.TABLE_NAME, c.COLUMN_NAME
    FROM INFORMATION_SCHEMA.TABLES AS t
    JOIN INFORMATION_SCHEMA.COLUMNS AS c ON c.TABLE_NAME = t.TABLE_NAME
    WHERE t.TABLE_TYPE = 'BASE TABLE'
    AND c.DATA_TYPE IN ('nvarchar', 'varchar', 'text', 'ntext');

    OPEN tabelaColuna_cursor;

    FETCH NEXT FROM tabelaColuna_cursor INTO @tabelaNome, @colunaNome;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @consulta = 'IF EXISTS (SELECT * FROM ' + QUOTENAME(@tabelaNome) + ' WHERE ' + QUOTENAME(@colunaNome) + ' LIKE ''%' + @palavraProcurada + '%'') '
                      + 'BEGIN '
                      + '    RAISERROR(''Tabela - %s, Coluna - %s'', 0, 0, @tabelaNome, @colunaNome) WITH NOWAIT; '
                      + 'END';

        EXEC sp_executesql @consulta;

        FETCH NEXT FROM tabelaColuna_cursor INTO @tabelaNome, @colunaNome;
    END;

    CLOSE tabelaColuna_cursor;
    DEALLOCATE tabelaColuna_cursor;
    """

    cursor.execute(script_sql)
    conn.commit()
    cursor.close()
    conn.close()

# Exemplo de uso:
server = 'your_server'
database = 'your_database'
palavra_procurada = 'sua_palavra'

procurar_palavra_em_tabelas(server, database, palavra_procurada)

# Exemplo de uso:
server = 'PAT-1620\SQLEXPRESS'
database = 'master'
palavra_procurada = 'gasolina'

procurar_palavra_em_tabelas(server, database, palavra_procurada)
