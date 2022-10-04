

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
        raise("Insufficient Arguments")
    
    outputName = sys.argv[1].rsplit("-",1)[0] + '-output1.txt'
    problems(outputName,calBody,calReadings,empivot,optpivot)

def problems(outputName,calBody,calReadings,empivot,optpivot):
    c_expected = q4.transformation(calBody,calReadings)
    

    fileOut = open(outputName,"w")
    fileOut.write('{0} , {1} , {2}\n'.format(len(c_expected[0].points[0]),len(c_expected),outputName))
    for frame in c_expected:
        for row in (frame.points.T):
            fileOut.write('{0} ,{1} ,{2}\n'.format(format(row[0],".2f"),format(row[1],".2f"),format(row[2],".2f")))
    fileOut.close()

if __name__ == "__main__":
    main()
