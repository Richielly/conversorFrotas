import os
class Base:
    
    def create_dir(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            return dir_name
        else:
            return dir_name

    def create_file_py(self, dir=r'C:\Users\Equiplano\PycharmProjects\conversorFrotas\venvconversorfrotas\Layout', file_name='default', content=''):

        if not os.path.exists(dir):
            os.makedirs(dir)
        file_path = os.path.join(dir, file_name+'.py')
        print(file_path)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)
            return file_path
        else:
            return False

    def replace_content_file_py(self, file_path, old_content, new_content):
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                new_line = line.replace(old_content, new_content)
                file.write(new_line)
            file.truncate()
        print(f"Conteúdo substituído em {file_path}")
