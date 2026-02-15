# начало
import os

os.listdir('.')
# ['.git', '.idea', '.venv', 'os_function.py', 'README.md'] - получен список папок и файлов в текущей
# директори , включая скрытые

os.rename('_testfile', 'testfile') # переименование файла  '_testfile' на 'testfile'

os.chmod('my_script.py', 0o777) # смена прав на файл

os.mkdir('new_dir') # создание нового каталога