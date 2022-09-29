
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
    problems(calBody,calReadings,empivot,optpivot)

def problems(calBody,calReadings,empivot,optpivot):
    q4.transformation(calBody,calReadings)
    


if __name__ == "__main__":
    main()
