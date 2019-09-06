#!/usr/bin/env python3
import psycopg2
import datetime

namedb = 'hostel'
users = 'admin'
pas = '123'

class Connect: 
    def __init__(self, namedb, users, pas):
        self.namedb = namedb
        self.users = users
        self.pas = pas

    def connectdb(self):
        conn_str = 'dbname='+self.namedb+' user='+self.users+' password='+self.pas
        conn = psycopg2.connect(conn_str) 
        return conn.cursor()
              
c1 = Connect(namedb, users, pas)
c = c1.connectdb()
         
field_name = '\n№ Rooms Lux Price DateIN DateOUT'
date_in = input('Введите дату заезда в формате(2000-01-01):')
date_out = input('Введите дату выезда в формате(2000-01-01):')
error_date = '\nВведите дату в правильном формате!!!' 

class Extract:
    def tell_all(self):
        c.execute("SELECT * FROM numbers;")
        rows = c.fetchall()
        print('\nВсе номера:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))
    
    def tell_lux(self):
        c.execute("SELECT * FROM numbers WHERE lux = True;")
        rows = c.fetchall()
        print('\nНомера класса люкс:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))
 
    def tell_rooms(self):
        c.execute("SELECT * FROM numbers WHERE room > 0;")
        rows = c.fetchall() 
        print('\nНомера c заданным количеством комнат:', field_name)
        for row in rows:
            print(" ".join(str(x) for x in row[1:]))

    def tell_count(self):
        try:
            c.execute("SELECT count(id) FROM numbers WHERE date_in > %s and date_out < %s", (date_in, date_out,))
            rows = c.fetchall()
            for row in rows:
                print ('\nКоличество занятых номеров:', row[0])
        except psycopg2.DataError:
            print(error_date)
        except psycopg2.InternalError:
            print(error_date)
  
    def tell_price(self):
        try:
            c.execute("SELECT sum(price) FROM numbers WHERE date_in > %s and date_out < %s", (date_in, date_out,))
            rows = c.fetchall()
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