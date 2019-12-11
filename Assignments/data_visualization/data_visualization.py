import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt


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
        rawMap[day] = text
        
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
totalDays:{} = {}
for day in days:
    total = 0
    for steps in days[day]:
        total += steps
    totalDays[day] = total

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
#Get interval array
x = np.array(intervals)
#add all steps to one list
steps:[int] = []
for day in days:
    steps.append(days[day])
y = np.array(rawSteps)
#np.reshape(y, (len(days), 288))

plt.plot(x,y)
#plt.show()

#Which 5-minute interval, on average across all the days in the dataset, contains the maximum number of steps?
index:int = -1
maxStep:int = -1
for i in range(len(rawSteps)):
    if int(rawSteps[i]) > int(maxStep):
        maxStep = rawSteps[i]
        index = i
print("Max steps: interval", intervals[index], " with", rawSteps[index], " steps")

#missing values
totalNA = 0
for day in rawMap:
    for data in rawMap[day]:
        if data == "NA":
            totalNA+=1
print("Total missing values:", totalNA)


csv_file.close()
