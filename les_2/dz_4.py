from cgitb import text
from fileinput import filename
from msvcrt import putch
from os import stat
import os
import shutil
from requests import request

import requests

links = []
filesLinks = ["robots.txt", "sitemap.xml"]

with open("les_2\dz_4_files\links.txt", "r", encoding="UTF-8") as sourceFile:
    links = sourceFile.read().split("\n")

for link in links:
    print(f"Сайт: {link}")

    for fileName in filesLinks:
        print(f"Файл: {fileName}")

        # Запрос к файлу сайта в потоке
        status = requests.get((str(link)+str(fileName)), stream=True)

        # Если статус 200, то все норм
        if  status.status_code == 200:
           puthFile = (link+fileName).split("/")
           puthFile = puthFile[2]+"-"+puthFile[3]
           with open(f"les_2\dz_4_files\{puthFile}", 'wb') as fileResult:
               status.raw.decode_content = True
               shutil.copyfileobj(status.raw, fileResult)
           print("OK")
        else:
          print("Ошибка: " + str(status.status_code))
    print("\n")    
    



"""
Напиши программу, которая проходит сайты по списку, 
скачивает файлы robots.txt и sitemap.xml и сохраняет на диск.
 В случае если файл не найден, выводится сообщение об этом.
"""

         