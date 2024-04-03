import json
import csv
d = {
    'apple': 'olma',
    'banana': 'banan',
    'orange': 'orik',
    'wotermelon': 'tarvuz'
}

with open('result.json', 'w') as file:
    json.dump(d, file, indent=4)

with open('result.json', 'r') as file:
    read_file = str(json.load(file))
    with open('res.txt', 'w') as file1:
        file1.write(read_file)
with open('res.txt', 'r') as file:
    print(dict(file.read))
    with open('new.csv', 'w') as newfile:
        writer = csv.writer(newfile)
        # writer.writerows(rf.items())



# with open('res.txt', 'r') as file:
#     data = file.read()
#     with open('new.csv', 'w') as file2:
#         d = csv.writer(file)
#         d.writerows(file2)
