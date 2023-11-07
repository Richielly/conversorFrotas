import configparser

from LayoutReader import bemLayoutReader_old as bemreader
# from LayoutReader import corLayoutReader as correader
# from LayoutReader import marcaLayoutReader as marcareader
# from LayoutReader import especieLayoutReader as especiereader
# from LayoutReader import tipoServicoLayoutReader as tipoServicoreader
# from LayoutReader import motoristaLayoutReader as motoristareader
# from LayoutReader import motoristaCategoriaCnhLayoutReader as motoristacategoriacnhreader
# from LayoutReader import motoristaSituacaoCnhLayoutReader as motoristasituacaocnhreader
from Core import imports

core = imports.core
file = imports.file

cfg = configparser.ConfigParser()
cfg.read(r'C:\Users\Equiplano\PycharmProjects\conversorFrotas\cfg.ini')

file_dir_bem =cfg['DEFAULT']['DiretorioArquivos'] + core.step['Bem'][3]
bem_file = file.file_read(file_dir_bem)
bem = bemreader.BemLayoutReader()
bem.run(bem_file)


# file_dir_marca =cfg['DEFAULT']['DiretorioArquivos'] + core.step['Marca'][3]
# marca_file = file.file_read(file_dir_marca)
# marca = marcareader.MarcaLayoutReader()
# marca.run(marca_file)
#
# file_dir_cor =cfg['DEFAULT']['DiretorioArquivos'] + core.step['Cor'][3]
# cor_file = file.file_read(file_dir_cor)
# cor = correader.CorLayoutReader()
# cor.run(cor_file)
#
# file_dir_especie =cfg['DEFAULT']['DiretorioArquivos'] + core.step['Especie'][3]
# especie_file = file.file_read(file_dir_especie)
# especie = especiereader.EspecieLayoutReader()
# especie.run(especie_file)
#
# file_dir_tipoServico =cfg['DEFAULT']['DiretorioArquivos'] + core.step['TipoServico'][3]
# tipoServico_file = file.file_read(file_dir_tipoServico)
# tipoServico = tipoServicoreader.TipoServicoLayoutReader()
# tipoServico.run(tipoServico_file)
#
# file_dir_motorista =cfg['DEFAULT']['DiretorioArquivos'] + core.step['Motorista'][3]
# motorista_file = file.file_read(file_dir_motorista)
# motorista = motoristareader.MotoristaLayoutReader()
# motorista.run(motorista_file)
#
# file_dir_motoristacategoriacnh =cfg['DEFAULT']['DiretorioArquivos'] + core.step['MotoristaCategoriaCnh'][3]
# motoristacategoriacnh_file = file.file_read(file_dir_motoristacategoriacnh)
# motoristacategoriacnh = motoristacategoriacnhreader.MotoristaCategoriaCnhLayoutReader()
# motoristacategoriacnh.run(motoristacategoriacnh_file)
#
# file_dir_motoristasituacaocnh =cfg['DEFAULT']['DiretorioArquivos'] + core.step['MotoristaSituacaoCnh'][3]
# motoristasituacaocnh_file = file.file_read(file_dir_motoristasituacaocnh)
# motoristasituacaocnh = motoristasituacaocnhreader.MotoristaSituacaoCnhLayoutReader()
# motoristasituacaocnh.run(motoristasituacaocnh_file)