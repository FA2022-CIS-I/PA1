

from distutils.log import error
import sys

def main():

    fileOne = sys.argv[1]
    fileTwo = sys.argv[2]
    print(sys.argv)
    file1 = open(fileOne, 'r')
    file2 = open(fileTwo,'r')
    linesOne = file1.readlines()
    linestwo = file2.readlines()
    #check if same length 
    if len(linesOne) != len(linestwo):
        error("Not the same Length")
    else: 
        for i in range(1,len(linesOne)):
            
            firstArray = linesOne[i].replace(" ", "").split(",")
            secondArray = linestwo[i].replace(" ", "").split(",")
            if(firstArray != secondArray):
                print("Not a Match at Line: " + str(i+1))
                print("First File "+str(firstArray))
                print("Seoncd File "+str(secondArray))



if __name__ == "__main__":
    main()