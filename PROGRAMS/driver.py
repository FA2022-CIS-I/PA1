

import sys
import q4 as q4
import q5 as q5
import q6 as q6


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
    outputName = outputName.replace("Input","Output")
    print(outputName)
    problems(outputName,calBody,calReadings,empivot,optpivot)

def problems(outputName,calBody,calReadings,empivot,optpivot):
    cExepcted = q4.transformation(calBody,calReadings)
    pivCalReadings = q5.getCalibrationReadings(empivot)
    optCalReadings = q6.getCalibrationReadings(optpivot)

    fileOut = open(outputName,"w")
    fileOut.write('{0} , {1} , {2}\n'.format(len(cExepcted[0].points[0]),len(cExepcted),outputName))
    fileOut.write('{0} ,{1} ,{2}\n'.format(format(pivCalReadings[0],".2f"),format(pivCalReadings[1],".2f"),format(pivCalReadings[2],".2f")))
    fileOut.write('{0} ,{1} ,{2}\n'.format(format(optCalReadings[0],".2f"),format(optCalReadings[1],".2f"),format(optCalReadings[2],".2f")))
    for frame in cExepcted:
        for row in (frame.points.T):
            fileOut.write('{0} ,{1} ,{2}\n'.format(format(row[0],".2f"),format(row[1],".2f"),format(row[2],".2f")))
    fileOut.close()

if __name__ == "__main__":
    main()
