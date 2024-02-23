# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(path):
    import os
    dirname, filename = os.path.split(path)
    basename, extension = os.path.splitext(filename)
    return (dirname, basename, extension)

path1 = "C:\Program Files\Adobe\Acrobat\Acrobat.exe"

print(split_path(path1))