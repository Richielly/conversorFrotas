from Core import imports
_file = imports.file
class Progress:

    def progress(self, file):
        lines = _file.file_read(file)
        return lines.shape[0]
