testCsvFile = "answersOutput1.csv"
mainCsvFile = "JEOPARDY_CSV.csv"
allCategories = {}

with open(mainCsvFile, "r", encoding="UTF8") as readFile:
    for line in readFile:
        contents = line.split(",")
        category = contents[3]
        #print(category)
        if category in allCategories:
            #print("found")
            allCategories[category] += 1
        else:
            #print("not found")
            allCategories[category] = 1
    readFile.close()

firstKey = ""
firstValue= 0
secondKey = ""
secondValue= 0
thirdKey = ""
thirdValue = 0
fourthKey = ""
fourthValue= 0
fifthKey = ""
fifthValue = 0
sixthKey = ""
sixthValue= 0
seventhKey = ""
seventhValue = 0
eighthKey = ""
eighthValue= 0
ninthKey = ""
ninthValue = 0
tenthKey = ""
tenthValue = 0


for key, value in allCategories.items():
    if value > firstValue:
        tenthValue = ninthValue
        tenthKey = ninthKey
        ninthValue = eighthValue
        ninthKey = eighthKey
        eighthValue = seventhValue
        eighthKey = seventhKey
        seventhValue = sixthValue
        seventhKey = sixthKey        
        sixthValue = fifthValue
        sixthKey = fifthKey
        fifthValue = fourthValue
        fifthKey = fourthKey
        fourthValue = thirdValue
        fourthKey = thirdKey
        thirdValue = secondValue
        thirdKey = secondKey
        secondValue = firstValue
        secondKey = firstKey
        firstValue = value
        firstKey = key

print(str(firstKey) + " : " + str(firstValue))
print(str(secondKey) + " : " + str(secondValue))
print(str(thirdKey) + " : " + str(thirdValue))
print(str(fourthKey) + " : " + str(fourthValue))
print(str(fifthKey) + " : " + str(fifthValue))
print(str(sixthKey) + " : " + str(sixthValue))
print(str(seventhKey) + " : " + str(seventhValue))
print(str(eighthKey) + " : " + str(eighthValue))
print(str(ninthKey) + " : " + str(ninthValue))
print(str(tenthKey) + " : " + str(tenthValue))

