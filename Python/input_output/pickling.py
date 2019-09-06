#!/usr/bin/env python3
import pickle

#имя файла в котором сохраним объект
shoplistfile = 'shoplist.data'
#Список пуст
shoplist = ['яблоки', 'манго', 'морковь']

#запись в файл
f = open(shoplistfile, 'w')
pickle.dump(shoplist, f) #помещаем объъект в файл
f.close()

del shoplist # уничтожаем переменную shoplist

# считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)

 