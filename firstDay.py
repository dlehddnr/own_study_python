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
# hours = input('Enter hours: ')
# money = input("Enter Rate: ")
# try:
#     fh = float(hours)
#     fm = float(money)
# except:
#     print('Error plz enter number')
#     quit()
# if fh > 40:
#     print('OverTime')
#     reg = fh * fm
#     ovt = (fh - 40.0) * (fm * 0.5)
#     pay = reg + ovt
# else:
#     print('RegularTime')
#     pay = fh * fm
# print('Pay:', pay)

#Practice5
# def com(fh, fm):
#     if fh > 40:
#         print('OverTime')
#         reg = fh * fm
#         ovt = (fh - 40.0) * (fm * 0.5)
#         pay = reg + ovt
#     else:
#         print('RegularTime')
#         pay = fh * fm
#     return pay
# hours = input('Enter hours: ')
# money = input("Enter Rate: ")
# try:
#     fh = float(hours)
#     fm = float(money)
# except:
#     print('Error plz enter number')
#     quit()

# pay = com(fh, fm)

# print('Pay:', pay)

#Counting
# count = 0
# print('before', count)
# for thing in [1, 2, 32, 44, 552, 61, 27, 83, 9]:
#     count = count + 1
#     print(count, thing)
# print('After', count)

#Total
# count = 0
# print('before', count)
# for thing in [1, 3, 42, 523, 324, 5, 3, 42, 5]:
#     count = thing + count
#     print(count, thing)
# print('after', count)

#Average
# count = 0
# num = 0
# print('before', count)
# for thing in [1, 3, 42, 523, 324, 5, 3, 42, 5]:
#     count = thing + count
#     num = num + 1
#     print(count, num)
# print('after', count / num)

#Finding Smallest
# smallest = None
# print('Before')
# for value in [3, 42, 12, 42, 4253, 52, 34, 1]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After', smallest)

# #Practice6
# num = 0
# tot = 0.0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid Input')
#         continue
#     num = num + 1
#     tot = tot + fval

# print(tot, num, tot / num)
