from cgitb import text
from requests import request

import requests

links = []

with open("les_2\dz_4_files\links.txt", "r", encoding="UTF-8") as sourceFile:
    links = sourceFile.read().split("\n")

for link in links:
    status = requests.get(str(link))











"""
Напиши программу, которая проходит сайты по списку, 
скачивает файлы robots.txt и sitemap.xml и сохраняет на диск.
 В случае если файл не найден, выводится сообщение об этом.
"""