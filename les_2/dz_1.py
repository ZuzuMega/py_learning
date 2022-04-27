import socket
from xml.sax.handler import property_interning_dict

ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
adrArray = []

# Открываем файл с адресами
with open('dz_1_files/adresses.txt', 'r', encoding='UTF-8') as adrFile:
    text = adrFile.read()
    # Адреса помещаем в массив
    adrArray = text.split('\n')

# Удаляем первую информационную строку файла из массива
adrArray.pop(0)

# Перечисляем адреса
print("Загружен список следующих адресов: ")
for adress in adrArray:
    print(adress)

# Открываем фалй для записи
resFile = open('dz_1_files/results.txt', 'w', encoding='UTF-8')
resFile.write("У следующих адресов имеется активные порты: ")

# Перебираем адреса
for adress in adrArray:
    # Перебираем порты для каждого адреса
    print("\nСканируется адрес: " + str(adress))
    resFile.write(str(adress)+"\n")
    for port in ports:
        soc = socket.socket()
        soc.settimeout(1)
        # Попытка коннекта
        try:
            soc.connect((adress, port))
        # Если коннекта нет, то порт пропускается
        except socket.error:
            pass
        # Если коннект есть, то запись в консоль и файл
        else:
            print(f"{adress}: {port} порт активен")
            soc.close
            resFile.write(str(port)+"\n")
    print("\n")
    
resFile.close()
print ("Сканирование завершено!")
            

'''
Сделай, чтобы сканер портов получал список IP из одного
 файла, а результаты сканирования записывал в другой.
'''