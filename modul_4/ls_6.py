import csv
import json

with open('actyor.csv') as file:
  data = list(csv.DictReader(file))
  with open('actyor.json', 'w') as file2:
    json.dump(data, file2, indent=4)

menu = """
1. actorlarni chiqarish
2. 1 ta actorni chiqarish
0. stop
"""

while True:
  n = input(menu)
  if n == '1':
    with open('actyor.json') as f:
      print(json.load(f))
  elif n == '2':
    _id = input('actor id sini kiriting : ')
    with open('actyor.json') as f:
      dat = list(json.load(f))
      for i in dat:
        if i['actor_id'] == _id:
          print(i)
          break
  elif n == '0':
    print('datstur tugadi')
    break