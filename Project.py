import statistics
import csv

with open('SOCR-HeightWeight.csv') as f :
    objectName = csv.reader(f)
    file_list = list(objectName)

file_list.pop(0)
weight_list = []

for i in range(len(file_list)) :
    weight = file_list[i][2]
    weight_list.append(float(weight))

mean = statistics.mean(weight_list)
print('Mean is equal to')
print(mean)

median = statistics.median(weight_list)
print('Median is equal to')
print(median)

mode = statistics.mode(weight_list)
print('Mode is equal to')
print(mode)

