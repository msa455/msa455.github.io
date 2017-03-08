import random

#choose a random file number
fileNumber = random.randint(1,22)
fileName = "answersOutput" + str(fileNumber) + ".csv"
#choose how many questions to ask the user
questions = 3
print("I will ask you 3 questions")

with open(fileName, "r", encoding="UTF8") as file:
    #create a directory of file offset positions to seek later
    fileList = list(file)
    #for each questions find a question from the text
    for x in range(questions):
        questionNumber = random.randint(1, len(fileList))
        question = (fileList[questionNumber]).split(",")
        print(question)
        print("CATEGORY: " + question[3])
        print("QUESTION: " + question[5])
