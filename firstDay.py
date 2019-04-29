print("hello world")

# Elabator
# inp = input("Europe Floor? ")
# usf = int(inp) + 1
# print('US floor', usf)

# Practice
# name = input('Enter your name: ')
# print('Hello', name)

# Practice2
# hours = input('Enter hours: ')
# money = input("Enter Rate: ")
# pay = float(hours) * float(money)
# print('Pay:', pay)

# Practice3
# hours = input('Enter hours: ')
# money = input("Enter Rate: ")
# fh = float(hours)
# fm = float(money)
# if fh > 40:
#     print('OverTime')
#     reg = fh * fm
#     ovt = (fh - 40.0) * (fm * 0.5)
#     pay = reg + ovt
# else:
#     print('RegularTime')
#     pay = fh * fm
# print('Pay:', pay)

# Practice4
hours = input('Enter hours: ')
money = input("Enter Rate: ")
try:
    fh = float(hours)
    fm = float(money)
except:
    print('Error plz enter number')
    quit()
if fh > 40:
    print('OverTime')
    reg = fh * fm
    ovt = (fh - 40.0) * (fm * 0.5)
    pay = reg + ovt
else:
    print('RegularTime')
    pay = fh * fm
print('Pay:', pay)
