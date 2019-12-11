import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt
import random

#Load csv file
csv_file = open('activity.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

#What is mean total number of steps taken per day?
linecount = 0
intervals = []
rawSteps = []
days:{} = {}
rawMap:{} = {}
for row in csv_reader:
    if linecount == 0:
        linecount+=1
    else:
        intervals.append(row[2])
        text:str = row[0]
        day:str = row[1]
        
        if day in rawMap:
            rawMap[day].append(text)
        else:
            rawMap[day] = [text]
        
        if text == "NA":
            rawSteps.append("0")
        else:
            rawSteps.append(int(text))  
        
        if day in days:
            if (text == "NA"):
                continue
            else:
                days[day].append(int(text)) 
        else:
            if (text == "NA"):
                continue
            else:
                days[day] = [int(text)]
#Total
def getTotalStepsPerDay(dataMap:{}) -> {}:
    totalDays:{} = {}
    for day in dataMap:
        total = 0
        for steps in dataMap[day]:
            total += steps
        totalDays[day] = total
    return totalDays
    totalDays[day] = total

totalDays:{} = getTotalStepsPerDay(days)

#Histogram
plt.bar(totalDays.keys(), totalDays.values(), 1.0, color='g')
plt.xticks(rotation = 45)
plt.show()

#Report
for day in days:
    print(day + ":")
    print("Mean:", statistics.mean(days[day]))
    print("Median:", statistics.median(sorted(days[day])))
    print()
    

#What is the average daily activity pattern?
#add all steps to one list
steps:{} = {}

for day in days:
    interval:int = 0
    for step in days[day]:   
        if interval in steps:
            steps[interval] += step
        else:
            steps[interval] = step
        
        interval += 5

for interval in steps:
    steps[interval] = steps[interval]//288    

x = np.array(list(steps.keys()))
y = np.array(list(steps.values()))
#np.reshape(y, (len(days), 288))

plt.plot(x,y)
plt.show()

#Which 5-minute interval, on average across all the days in the dataset, contains the maximum number of steps?
index:int = -1
maxStep:int = -1
for i in range(len(rawSteps)):
    if int(rawSteps[i]) > int(maxStep):
        maxStep = rawSteps[i]
        index = i
print("Max steps: interval", intervals[index], " with", rawSteps[index], " steps")

#calculate missing values
totalNA = 0
for day in rawMap:
    for data in rawMap[day]:
        if data == "NA":
            totalNA+=1
print("Total missing values:", totalNA)

#filling missing values
newValues:[int] = []
for i in range(totalNA):
    num:int = random.randint(0, 100)
    newValues.append(num)

#new dataset
newDataSet:{} = {}
index:int = 0
for day in rawMap:
    for steps in rawMap[day]:
        if day in newDataSet:
            if steps == "NA":
                newDataSet[day].append(newValues[index])
            else:
                newDataSet[day].append(int(steps))
        else:
            if steps == "NA":
                newDataSet[day] = [newValues[index]]
            else:
                newDataSet[day] = [int(steps)]

#Make new histogram
totalStepsNew:{} = getTotalStepsPerDay(newDataSet)
plt.bar(totalStepsNew.keys(), totalStepsNew.values(), 1.0, color='g')
plt.xticks(rotation = 90)
plt.show()
for day in newDataSet:
    print(day + ":")
    print("Mean:", statistics.mean(newDataSet[day]))
    print("Median:", statistics.median(sorted(newDataSet[day])))
    print()
    
#Weekends and weekdays
dayTypeMap:{} = {}
dayTypeMap["weekdays"] = []
dayTypeMap["weekends"] = []
counter:int = 1
for day in days:
    if counter == 8:
        counter = 1
    
    if counter < 6:
        dayTypeMap["weekdays"].append(day)
    else:
        dayTypeMap["weekends"].append(day)
    counter+=1

#Get interval array
#Sum steps in 5 minute intervals weekdays
steps:{} = {}
for day in newDataSet:
    if day in dayTypeMap["weekdays"]:
        interval:int = 0
        for step in newDataSet[day]:
            if interval in steps:
                steps[interval] += step
            else:
                steps[interval] = step
            interval += 5
#Average steps
for interval in steps:
    steps[interval] = steps[interval]//288
x = np.array(list(steps.keys()))
y = np.array(list(steps.values()))
#np.reshape(y, (len(days), 288))

plt.plot(x,y)
plt.show()

csv_file.close()
