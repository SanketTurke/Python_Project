class tooYoung(Exception):
    def __init__(self,msg):
        self.msg=msg

class tooOld(Exception):
    def __init__(self,msg):
        self.msg=msg

age = int(input("Enter the Age :"))
if age<18:
    raise tooYoung("u r too young to apply for licence")
elif age>70:
    raise tooOld('u r too old to apply for licence')
else:
    print('u r eligible')
