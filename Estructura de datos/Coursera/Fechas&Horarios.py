# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:15:35 2021

@author: MedNo
"""

import datetime
#Objetos de tipo date
date = datetime.date(2021, 10, 9)

date.year

date.month

date.day

date.weekday() #Lunes = 0 || Domingo = 6

date.isoweekday() #Lunes = 1 || Domingo = 7

date.isocalendar() #Devuelve ||año||num de semana||diaSemana

date.isoformat() #Pone la fecha como String

date_min = datetime.date.min #fecha minina

date_max = datetime.date.max #fecha maxina

today = datetime.date.today() #dia de hoy

yesterday = today - datetime.timedelta(days=1) #ayer

delta = today - yesterday #resta dos fechas



#Objetos de tipo datetime
date_and_time = datetime.datetime(2021, 10, 9, 9, 37, 30)

date_and_time.year

date_and_time.month

date_and_time.day

date_and_time.hour

date_and_time.minute

date_and_time.second

date_and_time.microsecond

date_and_time.date()

now = datetime.datetime.now()

now = datetime.datetime.utcnow()


#Objetos de tipo time

time = datetime.time(10, 20, 35)

time.hour

time.minute

time.second

time.microsecond

time_min = datetime.time.min

time_max = datetime.time.max
