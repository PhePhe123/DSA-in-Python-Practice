#Calculate Average Temperature

numDays = int(input("Enter number of days you would like to include: "))
totalTemp = 0
temps = []
for i in range(numDays):
    dailyTemp = int(input("Day " + str(i+1) + "'s high temp: "))
    temps.append(dailyTemp)
    totalTemp += temps[i]

averageTemp = round(totalTemp / numDays,2)
print("\nThe average temperature is " + str(averageTemp))

above = 0
for j in temps:
    if j > averageTemp:
        above += 1

print("\nThe number of days above average is " + str(above))


