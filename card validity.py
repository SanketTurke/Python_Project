from datetime import *
def cardValidity(expDate):
    if expDate>datetime.now().date():
        print('card is valid')
    else:
        print('card expired')
cardValidity(date(2022,11,1))