
from distutils.log import error
import sys
import q4 as q4
from numpy import empty


def main():

    # Placeholders for files
    calBody = None
    calReadings = None
    empivot = None
    optpivot = None

    # Check if appropriate amount of args
    if (len(sys.argv) == 5):
        # Assign
        calBody = sys.argv[1]
        calReadings = sys.argv[2]
        empivot = sys.argv[3]
        optpivot = sys.argv[4]
    else:
        error("Insufficient Arguments")
    problems(outputName,calBody,calReadings,empivot,optpivot)

def problems(outputName,calBody,calReadings,empivot,optpivot):
    c_expected = q4.transformation(calBody,calReadings)
    

    fileOut = open(outputName)


if __name__ == "__main__":
    main()
