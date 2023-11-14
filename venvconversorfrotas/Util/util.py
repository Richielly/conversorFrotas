from datetime import datetime
import configparser
import os
import shutil
class Util:

    def remove_spaces(self, text):
        return text.strip()

    def remove_all_spaces(self, text):
        return text.replace(" ", "")

    def remove_itens_in_list(self, list, itens_from_remove):
        for item in itens_from_remove:
            if item in list:
                list.remove(item)
        return list

    def remove_chars(self, string, chars):

        for char in chars:
            string = string.replace(char, "")
        return string
    def to_uppercase(self, text):
        return text.upper()

    def to_lowercase(self, text):
        return text.lower()

    def capitalize(self, text):
        return text.capitalize()

    def to_title(self, text):
        return text.title()

    def replace_substring(self,text, old, new):
        return text.replace(old, new)

    def complete_text(self, text, width, fillchar=' ', direction='left'):
        if direction == 'left':
            return text.ljust(width, fillchar)
        elif direction == 'right':
            return text.rjust(width, fillchar)
        else:
            raise ValueError("a direção deve ser 'left' ou 'right'")

    def truncate_text(self, text, length):
        return text[:length]

    def remove_spaces_from_tuple(self, tuple_data):
        return tuple(element.strip() if isinstance(element, str) else element for element in tuple_data)

    def remove_pipe_char(self, text):
        return text.replace("|", "")

    def valid_size(self, string, max_size):
        return len(string) <= max_size

    def set_current_seconds(self, dt):
        current_seconds = datetime.now().second
        return dt.replace(second=current_seconds)

    def set_current_seconds_and_milliseconds_firebird(self, date_str):
        # Convertendo a string para um objeto datetime
        dt = datetime.strptime(date_str, '%d/%m/%Y %H:%M')

        # Obtendo os segundos e milissegundos atuais
        current_seconds = datetime.now().second
        current_microseconds = datetime.now().microsecond
        current_milliseconds = int(current_microseconds / 1000)

        # Atualizando o objeto datetime com os segundos e milissegundos atuais
        updated_dt = dt.replace(second=current_seconds, microsecond=current_milliseconds * 1000)

        # Formatando o objeto datetime para a string no formato desejado
        return updated_dt.strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            content = f.read()
        return content

    def update_cfg(self, ini='cfg.ini',secao='DEFAULT', chave='CodEntidade', new=0):
        cfg = configparser.ConfigParser()
        cfg.read(ini)
        # Modifica um valor existente
        cfg.set(secao, chave, new)
        # Salva as alterações no arquivo de configuração
        with open(ini, 'w') as configfile:
            cfg.write(configfile)

    def move_file_if_exists(self,origem_directory, file_name, dest_directory):
        """
        Move um arquivo .txt para o diretório especificado se ele existir.

        :param file_name: Nome do arquivo a ser movido.
        :param dest_directory: Diretório de destino para onde o arquivo será movido.
        """
        # Verifica se o arquivo existe no diretório de trabalho atual
        if not os.path.isfile(origem_directory + file_name):
            print( f"O arquivo {file_name} não existe no diretório atual.")

        # Verifica se o diretório de destino existe, se não, cria
        if not os.path.isdir(dest_directory):
            os.makedirs(dest_directory)

        if os.path.isfile(dest_directory + file_name):
            os.remove(dest_directory + file_name)

        # Move o arquivo
        shutil.move(origem_directory + file_name, dest_directory)
        print( f"O arquivo {file_name} foi movido para {dest_directory}.")
