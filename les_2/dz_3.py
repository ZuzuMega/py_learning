
from asyncio.sslproto import _DO_HANDSHAKE
from posixpath import split
from tkinter import Y


comand = input("Для запуска программы напиши Y: ")

textSource = ""
emailArray = []
domainsArray = []

if comand.lower() == 'y':
    with open('les_2\dz_3_files\source_data.txt', 'r', encoding='UTF-8') as fileSource:
        textSource = fileSource.read()
    textArray = textSource.split("\n")
    # Получаем email-ы и домены
    for str in textArray:
        str = str.split("|")
        # Email-ы
        emailArray.append(str[1])
        # Домены
        email = str[1]
        domen = email.split("@")
        domainsArray.append(domen[1])
        
    # domensArray - теперь множество. Повторяющиеся элементы удалены
    domainsArray = set(domainsArray)
    for domain in domainsArray:
        # Создаем файл с названием домена
        file = open(f'les_2\dz_3_files\{domain}.txt', 'w', encoding='UTF-8')
        print("\n" + f"Обрабатываем домен {domain}")
        # Перебираем emails
        for email in emailArray:
            domainEmail = email.split("@")
            # Если домен email совпадает с текущим доменом, то email записывается в файл
            if domainEmail[1] == domain:
                file.write(email+"\n")
                print(f"{email} записан в файл домена {domain}")
        file.close()
    print("\n" + "Исходный файл обработан. Email-ы размещены по папкам")  
else:
    print("Программа завершила работу")



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