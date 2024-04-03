# import csv
# menu = """
# 1. Viloyatlar
# 2. Tumanlar
#     viloyat id sini kiriting:
# 0. chiqish
# """
# while True:
#     key = input(menu)
#     if key == '1':
#         with open('regions.csv', 'r') as file:
#             for i in csv.reader(file):
#                 if i[1] != 'name':
#                     print(i[0], i[1])
#     elif key == '2':
#         vil = input('viloyat id sini kiriting :')
#         with open('districts.csv', 'r') as file:
#             for i in csv.reader(file):
#                 if i[2] == vil:
#                     print(i[1])
#     else:
#         break
import csv
import json

# with open('regions.csv', 'r') as file:
#     with open('districts.csv', 'r') as file2:
#         r = []
#         for region in list(csv.reader(file))[1:]:
#             l = []
#             for district in list(csv.reader(file2))[1:]:
#                 if district[2] == region[0]:
#                     l.append(district[0])
#                     l.append(district[1])
#                     l.append(region[1])
#             r.append(l)
# r4 = open('re.csv', 'w')
# writer = csv.writer(r)
# writer.writerow(r)
# r4.close()


# data = {}
#
# with open('regions.csv', 'r') as file:
#     file2 = open('districts.csv', 'r')
#     for r in list(csv.reader(file))[1:]:
#         k = {}
#         for d in list(csv.reader(file2))[1:]:
#             if r[0] == d[-1]:
#                 k = data.get(r[1], {})
#                 k.update({d[0]:d[1]})
#                 data[r[1]] = k
#
#     file2.close()
# print(data)
# j = open('users.json', 'w')
# json.dump(data, j, indent=2)
# j.close()




# with open('regions.csv', 'r') as file:
#     with open('districts.csv', 'r') as file2:
#         reader = list(csv.reader(file))
#         districts = list(csv.reader(file2))
#         dic = {}
#         for r in reader[1:]:
#             res = ""
#             for d in districts[1:]:
#                 if r[0] == d[2]:
#                     res = res + d[1][0]
#             print(sorted(res))
#             dic[r[1]] = sorted(res)
#
#
# with open('ddaata.json', 'w') as file:
#     json.dump(dic, file, indent=4)

# import csv
# import json
#
# with open('users.json', 'r') as file:
#     with open('new.csv', 'w') as file2:
#         w = csv.writer(file2)
#         r = json.load(file)
#         w.writerows(r.items())


# manu = """
# 1. viloyatlar
# 2. tumanlar
#     viloyat idsini kiritasiz
# 0. chiqish
# """
#
# while True:
#     key = input(manu)
#     if key == '1':
#         with open('regions.csv', 'r') as file:
#             for i in list(csv.reader(file))[1:]:
#                 print(i[1])