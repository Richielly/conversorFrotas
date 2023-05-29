from LayoutReader import especieLayoutReader as reader
from Core import imports

file = imports.file

file_dir =r'D:\Conversao\Acacia\410\destino\Arquivos\Especie.txt'
especie_file = file.file_read(file_dir)

especie =  reader.EspecieLayoutReader()

especie.run(especie_file)