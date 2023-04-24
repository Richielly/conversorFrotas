from datetime import datetime
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

    def to_uppercase(self, text):
        return text.upper()

    def to_lowercase(self, text):
        return text.lower()

    def capitalize(self, text):
        return text.capitalize()

    def to_title(self, text):
        return text.title()

    def replace_substring(text, old, new):
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

    def set_current_seconds(self, datetime):
        current_seconds = datetime.now().second
        return dt.replace(second=current_seconds)

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            content = f.read()
        return content

