# with open('_file.txt', 'r') as file:
#     r = file.read()
#     r3 = ''
#     for i in range(len(r)):
#         if int(i) % 2 == 0:
#             r3 += '00'
#         else:
#             r3 += ''.join(r[i])
#     with open('_file.txt', 'w') as file2:
#         file2.write(r3)
import json
from random import random, randint

# class Exam:
#     def __init__(self, file, write, read, clear):
#         self.file = file
#         self.write = write
#         self.read = read
#         self.clear = clear
#
#     def write(self):

# import requests
#
# with open('file.json', "w") as file:
#     url = requests.get('https://jsonplaceholder.typicode.com/todos').json()
#     json.dump(url, file, indent=4)
#
#
# def func(name_file):
#     with open(name_file, "r") as file2:
#         l = []
#         t = json.load(file2)
#         for line in t:
#             if line['completed'] == True:
#                 l.append(line)
#         with open(name_file, "w") as file3:
#             json.dump(l, file3, indent=4)
#
#
# func("file.json")


# user = {
#     'id': 1,
#     'Fullname': 'Botirjon',
#     'Passport_id': 'M123456',
#     'Password': 1234,
#     'Balance': 50000,
#     'card_number': 8600030436489310
# }

# users = json.loads(open('file.json').read())
# menu_1 = '''1. Register
# 2. Login
# 3. Exit
# '''
# while True:
#     n = input(menu_1)
#     if n == '1':
#         r = {}
#         r['id'] = users[-1]['id'] + 1
#         r['Fullname'] = input('Enter your name: ')
#         r['Passport_id'] = input('Enter your passport_id: ')
#         for i in users:
#             if i['Passport_id'] == r['Passport_id']:
#                 print('id da xatolik bor')
#                 continue
#         r['Password'] = int(input('Enter your password: '))
#         r['Balance'] = 0
#         r['card_number'] = 8600 + randint(9999999999, 1000000000000)
#         users.append(r)
#         with open('file.json', 'w') as file:
#             json.dump(users, file, indent=4)
#     elif n == '2':
#         c_n = int(input('Enter your card number: '))
#         p = int(input('Enter your password: '))
#         for i in users:
#             if i['card_number'] == c_n and i['Password'] == p:
#                 menu_2 = '''1. Transfer money\n2. Balance\n3. log out\n'''
#                 mu = input(menu_2)
#                 if mu == '1':
#                     c_r = int(input('Enter your card number: '))
#                     for j in users:
#                         if j['card_number'] == c_r:
#                             print(j)
#                             s = int(input('summa: '))
#                             for i in users:
#                                 if i['card_number'] == j['card_number']:
#                                     i['Balance'] += s
#                                     print('Balancega sz kiritgan summa qo`shildi')
#                                     with open('file.json', 'w') as file:
#                                         json.dump(users, file, indent=4)
#                                     break
#                 elif mu == '2':
#                     print(i['Balance'])
#     elif n == '3':
#         break


