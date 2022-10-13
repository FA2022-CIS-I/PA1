

from distutils.log import error
import sys
import numpy as np

def main():

    fileOne = sys.argv[1]
    fileTwo = sys.argv[2]
    print(sys.argv)
    file1 = open(fileOne, 'r')
    file2 = open(fileTwo,'r')
    linesOne = file1.readlines()
    linestwo = file2.readlines()

    #output = fileOne.split(".")[0].replace("Input","Output")+"data.txt"
    #file3 = open(output,"w")
    all = []
    #check if same length 
    if len(linesOne) != len(linestwo):
        error("Not the same Length")
    else: 
        for i in range(1,len(linesOne)):
            
            firstArray = linesOne[i].replace(" ", "").replace("\n","").split(",")
            secondArray = linestwo[i].replace(" ", "").replace("\n","").split(",")

            first = np.array(firstArray).astype(float)
            second = np.array(secondArray).astype(float)
            all.append(np.sum(np.abs(first-second)))

            if i == 1 or i == 2:
                print("EM "+ str(np.sum(np.abs(first-second))))

          #  if(firstArray != secondArray):
          #      print("Mismatch at Line: " + str(i+1) + "\t" + "1 File "+str(firstArray) + "\t2 File "+str(secondArray))
          #      errorCount = errorCount + 1
    #print("Total Errors " + str(errorCount))
    print("Mean " + str(np.mean(all)))

    print("Std " + str(np.std(all)))

if __name__ == "__main__":
    main()