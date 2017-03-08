#define variables such as the file to read from, the file to write to
#and how many lines you want per file
csvFile = "JEOPARDY_CSV.csv"
outputFile = "answersOutput"
linesPerFile = 10000

#this function does the majority of the writing work
def fileWriter(readFile, writeFile, startLine, endLine, splitNumber, iteration):
    #open the file to write to and to read from
    with open(readFile, "r", encoding="UTF8") as fileToRead, open(writeFile, "w", encoding="UTF8") as fileToWrite:
        print("writing " + str(splitNumber) + " lines from " + readFile + "to " + writeFile)
        print("start line: " + str(startLine))
        print("end line : " + str(endLine))
        #specify the line you are currently on in the file, starting at 0
        currentLine = 0
        #iterate through the file
        startMessage = False
        writeMessage = False
        for line in fileToRead:
            #if(currentLine % 1000 == 0):
                #print(currentLine)    
            currentLine += 1
            #if you are still before you should be in the file
            if(currentLine < startLine):
                if(startMessage != True):                
                    #print("catching up to the start line")
                    startMessage = True
                #don't do anything, just let the iterator continue
                pass
            #if you are between the startline and end line, where it should be
            elif(currentLine >= startLine and currentLine < endLine):
                #write that line from the readfile to the writefile
                if(writeMessage != True):
                    #print("writing the lines")
                    writeMessage = True
                fileToWrite.write(line)
            #if you are past where you should be writing
            else:
                #close your files and end the function returning false
                fileToRead.close()
                fileToWrite.close()
                print("completed splitting this file")
                return(False)
        #if there are no lines left in the document you are reading from
        else:
            #close the files you are working with and end the function returning true
            fileToRead.close()
            fileToWrite.close()
            print("completed splitting all files")
            return(True)


def main():
    #initally specify the function is not complete
    complete = False
    #initial iteration is 1
    iteration = 1
    #run this loop until the read file has been completely read
    while(complete != True):
        #specify where the function should start reading from
        start = (iteration - 1) * linesPerFile
        end = start + linesPerFile
        #print("working on iteration " + str(iteration))
        #specify the location of the file you will write to
        newWriteFile = outputFile + str(iteration) + ".csv"
        #call the function
        completion = fileWriter(csvFile, newWriteFile, start, end, linesPerFile, iteration)
        #add to the iteration count as the function finishes a cycle
        iteration = iteration + 1
        #set the complete value to see whether the loop is complete
        complete = completion
        
    #let the user know the program has finished running
    print("operation completed")

main()
