import os
import flet as ft
import configparser

from Data import conectBd
from Core import imports
from Util import util, script_analise_destino
from LayoutReader import bemLayoutReader as bemReader
from LayoutReader import tombamentoBemLayoutReader as tombamento_bemReader
from LayoutReader import saldoAnteriorBemLayoutReader as saldo_anterior_bemReader

utl = util.Util()

conn = conectBd.ConectBd()
cursor = conn.connection()

core = imports.core
file = imports.file

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
entidade = cfg['DEFAULT']['nomeentidade']
txt_header = ''

utl.update_cfg(secao='DEFAULT', chave='dir',new=os.getcwd())
utl.update_cfg(secao='DEFAULT', chave='diretorioarquivoslog',new=f'{os.getcwd()}\Logs\\')
utl.update_cfg(secao='DEFAULT', chave='diretorioarquivosprocessados',new=f'{os.getcwd()}\Processados\\')
def pages(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.title = "Importador dos Bens "+ str(entidade) + " V_1.8.0"
    progressBar = ft.ProgressBar(width=700, color=ft.colors.GREEN_ACCENT_700)

    def sincronizar(e):
        page.update()
        utl.update_cfg(secao='DEFAULT', chave='nomebanco', new=txt_database.value)
        utl.update_cfg(new=txt_entidade.value)
        cfg.read('cfg.ini')
        sqls = script_analise_destino.Script().query(txt_entidade.value)
        analise_data = {}
        if cursor:
            for sql in sqls.items():
                cursor.execute(sql[1])
                analise_data[sql[0]] = cursor.fetchone()
            txt_origem_bem = cfg['DEFAULT']['DiretorioArquivos'] + core.step['Bem'][3]
            if os.path.isfile(txt_origem_bem):
                bem_file = file.file_read(txt_origem_bem)
                analise_bem_origem.value = bem_file.shape[0]
            analise_bem_destino.value  = str(analise_data['Bem'][0])
            txt_origem_tombamento = cfg['DEFAULT']['DiretorioArquivos'] + core.step['TombamentoBem'][3]
            if os.path.isfile(txt_origem_tombamento):
                tombamento_file = file.file_read(txt_origem_tombamento)
                analise_tombamento_origem.value = tombamento_file.shape[0]
            analise_tombamento_destino.value = str(analise_data['TombamentoBem'][0])
            txt_origem_saldoanterior = cfg['DEFAULT']['DiretorioArquivos'] + core.step['SaldoAnteriorBem'][3]
            if os.path.isfile(txt_origem_saldoanterior):
                saldoanterior_file = file.file_read(txt_origem_saldoanterior)
                analise_saldo_anterior_bem_origem.value = saldoanterior_file.shape[0]
            analise_saldo_anterior_bem_destino.value = str(analise_data['SaldoAnteriorBem'][0])

            page.update()

    def btn_click(e):
        if not txt_database.value:
            txt_database.error_text = "Informe o caminho do Banco"
            page.update()
        page.add(progressBar)
        btn_gerar_arquivos.disabled = True
        utl.update_cfg(secao='DEFAULT', chave='diretorioarquivos', new=f'{txt_local_arquivos.value}')
        utl.update_cfg(new=txt_entidade.value)
        cfg.read('cfg.ini')

        page.add(txt_header)
        file_dir_bem = cfg['DEFAULT']['DiretorioArquivos'] + core.step['Bem'][3]
        if os.path.isfile(file_dir_bem):
            txt_header.value = "Arquivo Bem Executando..."
            bem_file = file.file_read(file_dir_bem)
            for linha in range(1, bem_file.shape[0] + 1):
                linha_data = file.lines_file(bem_file, linha)
                bem = bemReader.BemLayoutReader()
                if bem.run(linha_data, linha):
                    analise_bem_convertido.value = str(int(analise_bem_convertido.value) + 1)
                txt_header.value = f"Arquivo Bem Executando {linha}/{bem_file.shape[0]}"
                page.update()
            utl.move_file_if_exists(cfg['DEFAULT']['DiretorioArquivos'], core.step['Bem'][3], cfg['DEFAULT']['diretorioarquivosprocessados'])

        page.add(txt_header)
        file_dir_tombamento_bem = cfg['DEFAULT']['DiretorioArquivos'] + core.step['TombamentoBem'][3]
        if os.path.isfile(file_dir_tombamento_bem):
            txt_header.value = "Arquivo Tombamento Bem Executando..."
            tombamento_bem_file = file.file_read(file_dir_tombamento_bem)
            for linha in range(1, tombamento_bem_file.shape[0] + 1):
                linha_data = file.lines_file(tombamento_bem_file, linha)
                tombamento_bem = tombamento_bemReader.TombamentoBemLayoutReader()
                if tombamento_bem.run(linha_data, linha):
                    analise_tombamento_convertido.value = str(int(analise_tombamento_convertido.value) + 1)
                txt_header.value = f"Arquivo Tombamento Bem Executando {linha}/{tombamento_bem_file.shape[0]}"
                page.update()
            utl.move_file_if_exists(cfg['DEFAULT']['DiretorioArquivos'], core.step['TombamentoBem'][3], cfg['DEFAULT']['diretorioarquivosprocessados'])

        page.add(txt_header)
        file_dir_saldo_anterior_bem = cfg['DEFAULT']['DiretorioArquivos'] + core.step['SaldoAnteriorBem'][3]
        if os.path.isfile(file_dir_saldo_anterior_bem):
            txt_header.value = "Arquivo Saldo Anterior do Bem Executando..."
            saldo_anterior_bem_file = file.file_read(file_dir_saldo_anterior_bem)
            for linha in range(1, saldo_anterior_bem_file.shape[0] + 1):
                linha_data = file.lines_file(saldo_anterior_bem_file, linha)
                saldo_anterior_bem = saldo_anterior_bemReader.SaldoAnteriorBemLayoutReader()
                if saldo_anterior_bem.run(linha_data, linha):
                    analise_saldo_anterior_bem_convertido.value = str(int(analise_saldo_anterior_bem_convertido.value) + 1)
                txt_header.value = f"Arquivo Saldo Anterior do Bem Executando {linha}/{saldo_anterior_bem_file.shape[0]}"
                page.update()
            utl.move_file_if_exists(cfg['DEFAULT']['DiretorioArquivos'], core.step['SaldoAnteriorBem'][3], cfg['DEFAULT']['diretorioarquivosprocessados'])

        txt_header.value = "Conversão Finalizado"
        btn_gerar_arquivos.disabled = False
        page.add(txt_header)
        progressBar.value = 100
        page.update()

    page.add(ft.Text("Importador", size=20, color='green'))
    header_frotas = ft.Text("Importador", size=20, color='green')
    txt_entidade = ft.TextField(label="Entidade", text_size=12, value=cfg['DEFAULT']['CodEntidade'], width=100, height=35, disabled=False, tooltip='Alterar o código de entidade, tambem altera o arquivo "cfg.ini"')
    txt_host = ft.TextField(label="Host", text_size=12, value=cfg['DEFAULT']['Host'], width=100, height=35)
    txt_user = ft.TextField(label="User", text_size=12, value=cfg['DEFAULT']['User'], width=250, height=35)
    txt_password = ft.TextField(label="Password", text_size=12, value=cfg['DEFAULT']['password'], width=130, height=35,password=True, can_reveal_password=True)
    txt_database = ft.TextField(label="Caminho do Banco destino", value=cfg['DEFAULT']['NomeBanco'], text_size=12, height=50, width=700)
    txt_local_arquivos = ft.TextField(label="Caminho dos Arquivos para Importação", value=cfg['DEFAULT']['DiretorioArquivos'], text_size=12, height=40, width=700)
    txt_port = ft.TextField(label="Porta", text_size=12, value=cfg['DEFAULT']['port'], width=100, height=30)
    txt_header = ft.Text('Arquivos Importados')
    dados_banco = ft.Row([txt_entidade, txt_host, txt_port, txt_user, txt_password])
    btn_gerar_arquivos = ft.ElevatedButton("Importar", on_click=btn_click, icon=ft.icons.PLAY_CIRCLE)
    list_arquivos = ft.ListView(expand=1, spacing=2, padding=20, auto_scroll=True)
    divisor = ft.Divider(height=2, thickness=3)

    analise_bem_label = ft.Text("Bem", size=30, color='purple')
    analise_bem_origem = ft.Text("0", size=30, color='green')
    analise_bem_destino = ft.Text("0", size=30, color='blue')
    analise_bem_convertido = ft.Text("0", size=30, color='red')

    analise_tombamento_label = ft.Text("Tombamento", size=30, color='purple')
    analise_tombamento_origem = ft.Text("0", size=30, color='green')
    analise_tombamento_destino = ft.Text("0", size=30, color='blue')
    analise_tombamento_convertido = ft.Text("0", size=30, color='red')

    analise_saldo_anterior_bem_label = ft.Text("Saldo Anterior", size=30, color='purple')
    analise_saldo_anterior_bem_origem = ft.Text("0", size=30, color='green')
    analise_saldo_anterior_bem_destino = ft.Text("0", size=30, color='blue')
    analise_saldo_anterior_bem_convertido = ft.Text("0", size=30, color='red')

    #############################
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Tabela")),
            ft.DataColumn(ft.Text("Origem")),
            ft.DataColumn(ft.Text("Destino")),
            ft.DataColumn(ft.Text("Covertido")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(analise_bem_label),
                    ft.DataCell(analise_bem_origem),
                    ft.DataCell(analise_bem_destino),
                    ft.DataCell(analise_bem_convertido),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(analise_tombamento_label),
                    ft.DataCell(analise_tombamento_origem),
                    ft.DataCell(analise_tombamento_destino),
                    ft.DataCell(analise_tombamento_convertido),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(analise_saldo_anterior_bem_label),
                    ft.DataCell(analise_saldo_anterior_bem_origem),
                    ft.DataCell(analise_saldo_anterior_bem_destino),
                    ft.DataCell(analise_saldo_anterior_bem_convertido),
                ],
            ),
        ],
    )



    #############################

    btn_sincronizar_banco = ft.ElevatedButton("Sincronizar", on_click=sincronizar, icon=ft.icons.UPGRADE)

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,

        tabs=[
            ft.Tab(
                text="Importador",
                icon=ft.icons.DOWNLOADING,
                content=ft.Container(
                                    content=ft.Column([header_frotas, divisor, dados_banco, txt_database,txt_local_arquivos, btn_gerar_arquivos]),
                                    alignment=ft.alignment.center,
                                    padding=15
                                    ),
            ),
            ft.Tab(
                text="Analise",
                icon=ft.icons.MULTILINE_CHART,
                content=ft.Container(
                                    content=ft.Column([btn_sincronizar_banco, tabela],alignment=ft.alignment.center),
                                    alignment=ft.alignment.center,
                                    padding=50,
                                    border_radius=10,
                                    bgcolor=ft.colors.GREY_200,
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)
    list_arquivos = ft.ListView(expand=1, spacing=2, padding=20, auto_scroll=True)


if __name__ == "__main__":
    # ft.app(port=3636, target=main, view=ft.WEB_BROWSER)
    ft.app(target=pages)

#  pyinstaller --name Importador_Bem_V_1.0.0 --onefile --icon=bau.ico --noconsole app.py
# flet pack --name Importador_Bem_V_1.8.1 --icon=bau.ico app.py