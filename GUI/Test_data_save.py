import Data
import time
from time import gmtime, strftime

# currentDate = (time.strftime("%Y%m%d"))
# currentTime = time.strftime("%H%M%S")
NOW =  time.strftime("%Y%m%d%H%M%S")

print NOW , type(NOW)

date = NOW[0:4]
print date
# (self , Date = '' , Time = '' , Target_A = None , Max_A = None , Duration_hold = None , Score = None , Comment = '' ):
#
# Ex1 = Data.Puppies(currentDate, 'time', '70', '70', '70', '70', 'was really easy')
# Data.saveObject('Data_backend.txt', Ex1)