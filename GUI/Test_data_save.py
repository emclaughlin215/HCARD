import Data
import time
import datetime
from time import gmtime, strftime

currentDate = (time.strftime("%Y%m%d"))
# currentTime = time.strftime("%H%M%S")
# NOW =  time.strftime("%Y%m%d")
#
# print NOW , type(NOW)
#
# date = NOW[0:4]
# print date
# (self , Date = '' , Time = '' , Target_A = None , Max_A = None , Duration_hold = None , Score = None , Comment = '' ):
#
Ex1 = Data.Exercises(currentDate, '70', '10', '3', 'was really easy', 'keep it up')
Data.saveObject('Data_backend.txt', Ex1)

# datetime_object = datetime.datetime.strptime('09032018', '%d%m%Y')
# new_date = datetime_object + datetime.timedelta(days=7)
# print datetime_object , new_date
#
# new_date_string = new_date.strftime('%d%m%Y')
#
# print new_date_string