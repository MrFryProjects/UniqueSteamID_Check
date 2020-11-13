import json

filePath = 'C:\\Users\\Code\\Desktop\\'
fileName = 'SORTED_FIX_FriendsDepth3.json'

data = []
uniqueData = []

with open(filePath + fileName,'r') as file:
    data = json.load(file)

uniqueData.append(data[0])

lenData = len(data)

for i in range(len(data)):
    if uniqueData[-1] != data[0]:
        uniqueData.append(data.pop(0))
    elif uniqueData[-1] == data[0]:
        del data[0]

lenUData = len(uniqueData)

print(str(lenData - lenUData) + " duplicates eliminated")

with open(filePath + 'UNIQUE_' + fileName, 'w') as file:
    json.dump(uniqueData, file)