import csv

with open("height-weight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

#sorting to get the height
new_data=[]
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))


#mean
n = len(new_data)
sum = 0
for x in new_data:
    sum=sum+x
mean = sum/n
print("mean ="+ str(mean))