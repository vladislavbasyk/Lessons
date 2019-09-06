#!/usr/bin/env python3
import psycopg2
import datetime

conn = psycopg2.connect("dbname=hostel user=admin password=123")
cur = conn.cursor()

# class Connect:
#     def connectdb(self):
#         conn = psycopg2.connect("dbname=hostel user=admin password=123")
#         cur = conn.cursor()
        
         

field_name = '\n№ Rooms Lux Price DateIN DateOUT'
date_in = input('Введите дату заезда в формате(2000-01-01):')
date_out = input('Введите дату выезда в формате(2000-01-01):')
error_date = '\nВведите дату в правильном формате!!!'

class Extract:  
    def tell_all(self):
        cur.execute("SELECT * FROM numbers;")
        rows = cur.fetchall()
        print('\nВсе номера:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))
    
    def tell_lux(self):
        cur.execute("SELECT * FROM numbers WHERE lux = True;")
        rows = cur.fetchall()
        print('\nНомера класса люкс:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))
 
    def tell_rooms(self):
        cur.execute("SELECT * FROM numbers WHERE rooms > 0;")
        rows = cur.fetchall() 
        print('\nНомера c заданным количеством комнат:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))

    def tell_count(self):
        try:
            cur.execute("SELECT count(id) FROM numbers WHERE date_in > %s and date_out < %s", (date_in, date_out,))
            rows = cur.fetchall()
            for row in rows:
                print ('\nКоличество занятых номеров:', row[0])
        except psycopg2.DataError:
            print(error_date)
        except psycopg2.InternalError:
            print(error_date)
  
    def tell_price(self):
        try:
            cur.execute("SELECT sum(price) FROM numbers WHERE date_in > %s and date_out < %s", (date_in, date_out,))
            rows = cur.fetchall()
            for row in rows:
                print('\nОбщая стоимость занятых номеров:', row[0])        
        except psycopg2.DataError:
            print(error_date)
        except psycopg2.InternalError:
            print(error_date)             

e = Extract()
e.tell_all()
e.tell_lux()
e.tell_rooms()
e.tell_count()
e.tell_price()

         



