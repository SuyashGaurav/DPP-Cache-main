import pandas as pd
import random

path = "Datasets/311_dataset.txt"

data = pd.read_csv(path, sep = ' ')
data.columns = ['Timestamp', 'File_ID', "File_Size"]
DataLength = len(data)

# arr = [[0, i] for i in range(423)]
# for i in range(len(data)):
#     arr[(data["File_ID"][i])][0] += 1

# arr.sort(reverse=True)
# arr = arr[: 75]
# random.shuffle(arr)
# lastTime = max(data["Timestamp"])
# timediff = lastTime//100

for j in range(len(data)):
    data["File_ID"][j] = random.randint(1, 423)
# for i in range(50):
#     for j in range(len(data)):
#         if data["File_ID"][j] == arr[i][1]:
#             start = random.randint(0, lastTime-timediff)
#             num1 = random.randrange(start, start+timediff)
#             num2 = random.randrange(start+timediff, lastTime)
#             data["Timestamp"][j] = random.choices([num1, num2], weights=(4/5, 1/5), k = 1)[0]
# data.to_csv('dataset.csv')
# data = data.sort_values(by=['Timestamp'])
# data = pd.read_csv('dataset.csv')
f = open("randomDataSet.txt", "w")
for i in range(len(data)):
    f.write(str(data['Timestamp'][i]))
    f.write(" ")
    f.write(str(data['File_ID'][i]))
    f.write(" ")
    f.write(str(data['File_Size'][i]))
    f.write("\n")
f.close()