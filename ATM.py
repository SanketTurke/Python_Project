import sys
lst=sys.argv
account_balance=10000
q=("1.check balance")
print(q)
w=("2.withdraw")
print(w)
e=("3.deposite cash")
print(e)
r=("4.deposite check")
print(r)
a=(int(input("select the no.:")))
print(a)
if a==1:
    print("Balance:",account_balance)
elif a==2:
    s=(int(input("Enter Amount:")))
    print(s)
    print("Balance:",account_balance-s)
elif a==3:
    d=(int(input("Enter Amount:")))
    print(d)
    print("Balance:",d+account_balance)
elif a==4:
    f=(int(input("Enter Amount:")))
    print(f)
    print("Balance:",f+account_balance)