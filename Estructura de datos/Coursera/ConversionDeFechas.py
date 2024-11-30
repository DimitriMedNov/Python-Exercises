# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:52:21 2021

@author: MedNo
"""

import datetime

date_and_time = datetime.datetime(2021, 10, 9, 9, 37, 30)

#de string a objeto datetime

date_and_time.strftime('%Y-%m-%d')

date_and_time.strftime('%Y-%m-%d %H:%M:%S')

date_and_time.strftime('%Y/%m/%d')

date_and_time.strftime('%Y-%m-%d T%H:%M:%S')

#de objeto datetime a String

date_and_time.strptime('2021-10-9','%Y-%m-%d')

date_and_time.strptime('2021-10-9 9:37:30','%Y-%m-%d %H:%M:%S')

date_and_time.strptime('2021-10-9 T9:37:30','%Y-%m-%d T%H:%M:%S')
