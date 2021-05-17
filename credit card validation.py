from datetime import date

import datetime
from datetime import *

def creditValidation(expDate):
    if expDate>datetime.now().date():
        print("card is valid")
    else:
        print("card is expired")

dt = creditValidation(date())
print(dt)