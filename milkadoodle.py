#Declaring Arrays

amountOfCows = []
cowid = []
cowyield = []
yieldAmountDay1 = []
yieldAmountDay2 = []
yieldAmountDay3 = []
yieldAmountDay4 = []
yieldAmountDay5 = []
yieldAmountDay6 = []
yieldAmountDay7 = []
allMilkedLiters = ()

n = int(input("How many cows do you have? " ))
a = 1
for i in range(n):
    print("Input the ID of COW " + str(a) + ": ")
    CowIDarray = input()
    a = a + 1
    
    #Gathering Data

    CowIDYieldDay1 = int(input("Input day1 yield for the same cow's ID: "))
    yieldAmountDay1.append(CowIDYieldDay1)

    CowIDYieldDay2 = int(input("Input day2 yield for the same cow's ID: "))
    yieldAmountDay2.append(CowIDYieldDay2)

    CowIDYieldDay3 = int(input("Input day3 yield for the same cow's ID: "))
    yieldAmountDay3.append(CowIDYieldDay3)

    CowIDYieldDay4 = int(input("Input day4 yield for the same cow's ID: "))
    yieldAmountDay4.append(CowIDYieldDay4)

    CowIDYieldDay5 = int(input("Input day5 yield for the same cow's ID: "))
    yieldAmountDay5.append(CowIDYieldDay5)
    
    CowIDYieldDay6 = int(input("Input day6 yield for the same cow's ID: "))
    yieldAmountDay6.append(CowIDYieldDay6)
    
    CowIDYieldDay7 = int(input("Input day7 yield for the same cow's ID: "))
    yieldAmountDay7.append(CowIDYieldDay7)
    
    amountOfCows.append(CowIDarray)

totalYieldDay1 = sum(yieldAmountDay1)
totalYieldDay2 = sum(yieldAmountDay2)
totalYieldDay3 = sum(yieldAmountDay3)
totalYieldDay4 = sum(yieldAmountDay4)
totalYieldDay5 = sum(yieldAmountDay5)
totalYieldDay6 = sum(yieldAmountDay6)
totalYieldDay7 = sum(yieldAmountDay7)

weektotal = int(totalYieldDay1) + int(totalYieldDay2) + int(totalYieldDay3) + int(totalYieldDay4) + int(totalYieldDay5) + int(totalYieldDay6) + int(totalYieldDay7)


print("Cow ID's")
print(amountOfCows)
print(yieldAmountDay1, "Yield on Day 1 for each cow")
print(yieldAmountDay2, "Yield on Day 2 for each cow")
print(yieldAmountDay3, "Yield on Day 3 for each cow")
print(yieldAmountDay4, "Yield on Day 4 for each cow")
print(yieldAmountDay5, "Yield on Day 5 for each cow")
print(yieldAmountDay6, "Yield on Day 6 for each cow")
print(yieldAmountDay7, "Yield on Day 7 for each cow")
print("    ")
print("Total Yields for Each Day")
print("    ")
print(totalYieldDay1, "Liters milked on day 1")
print(totalYieldDay2, "Liters milked on day 2")
print(totalYieldDay3, "Liters milked on day 3")
print(totalYieldDay4, "Liters milked on day 4")
print(totalYieldDay5, "Liters milked on day 5")
print(totalYieldDay6, "Liters milked on day 6")
print(totalYieldDay7, "Liters milked on day 7")
print(weektotal, "total milk for a week")
