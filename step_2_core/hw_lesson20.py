# использую данную библиотеку что бы считать файл в UTF-8.
import codecs
fw = codecs.open("C:\\Users\\admin\\Downloads\\filefile.txt", "r", "utf_8_sig")
text = fw.read()
print(text)
# после считывания давайте посчитаем сколько символов в данном файле.
chars = len(text)
print(f'Количество символов в файле равно = {chars}')
# Запишем что-то в конец файла
fw = codecs.open("C:\\Users\\admin\\Downloads\\filefile.txt", "a", "utf_8_sig")
fw.write(input("Добавьте текст в файл :"))
chars = len(text)
fw.close()
print('Файл успешно обновлен')