

from asyncio.sslproto import _DO_HANDSHAKE


comand = input("Для запуска программы напиши Y: ")

textSource ="qweqwy"

if comand.lower() == 'y':
    with open('les_2\dz_3_files\source_data.txt', 'r', encoding='UTF-8') as fileSource:
        textSource = fileSource.read()
    textArray = textSource.split("\n")
    for str in textArray:
        ### ...
else:
    print("Программа завершила работу")






    # Zapis - w


"""
Напиши программу, которая читает файл такого вида:

    Иван Иванов|ivanov@mail.ru|Password123
    Дима Лапушок|superman1993@xakep.ru|1993superman
    Вася Пупкин|pupok@yandex.ru|qwerty12345
    Фродо Бэггинс|Frodo@mail.ru|MoRdOr100500
    Кевин Митник|kevin@xakep.ru|dontcrackitplease
    Юзер Юзерович|uswer@yandex.ru|aaaa321

Программа должна сортировать строки по доменам из email, для каждого домена 
создавать файл и в каждый файл помещать список почтовых адресов.
"""