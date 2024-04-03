# class Kalkulator():
#     def __init__(self, num1, belg, num2):
#         self.num1 = num1
#         self.num2 = num2
#         self.belg = belg
#
#     def r(self):
#         if self.belg == '+':
#             return self.num1 + self.num2
#         elif self.belg == '-':
#             return self.num1 - self.num2
#         elif self.belg == '*':
#             return self.num1 * self.num2
#         elif self.belg == '/':
#             return self.num1 / self.num2
#
#
# n1, b, n2 = input().split()
# r = Kalkulator(int(n1), b, int(n2))
# print(r.r())


import requests
url = requests.get('https://www.google.com/search?channel=fs&client=ubuntu-sn&q=ob+havo')
print(url.status_code)