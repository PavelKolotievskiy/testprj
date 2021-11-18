# Создать скрипт, который через параметр запуска получает имя исполняемого файла. И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не может быть запущен и т.д.) сделать через исключения.
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--exec', help='name of exe')

args = parser.parse_args()
exe_name = args.exec
# exe_name = 'menu.md'

try:
    subprocess.run(exe_name, stdout=subprocess.PIPE)
except FileNotFoundError:
    print("File not Found")
except OSError:
    print("File is not runnable")
except TypeError:
    print("Enter the Filename")
else:
    print("Something wrong")

# Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге было распечатано).
import logging
import os
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def file_list(path):
    cnt = 0
    for f in os.listdir(path):
        if os.path.isfile(f):
            print(f)
            cnt += 1
    logging.debug('file_list path:' + path)
    logging.debug('file_list count:' + str(cnt))


file_list('D:/git/test2')

# Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com. Скачанную информацию надо сохранить в файл.
import requests
import threading, queue


def download(url, result):
    r = requests.get(url)
    result.put(r.text)


results = queue.Queue()
t = threading.Thread(target=download, args=('https://epam.com', results,))
t.daemon = True
t.start()
t.join()

w = results.get()

result_file=open("result.html",mode="w",encoding="utf-8")
result_file.write(w)

