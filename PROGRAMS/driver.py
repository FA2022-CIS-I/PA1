

import sys
import q4 as q4
import q5 as q5
import q6 as q6


def main():
    """
        Main, primary driver, returns nothing
    """

    # Placeholders for files
    calBody = None
    calReadings = None
    empivot = None
    optpivot = None


    # Check if appropriate amount of args, must contains all specified file names as above
    if (len(sys.argv) == 5):
        # Assign
        calBody = sys.argv[1]
        calReadings = sys.argv[2]
        empivot = sys.argv[3]
        optpivot = sys.argv[4]
    else:
        raise("Insufficient Arguments")
    
    #Generate the output name for the given set of files
    outputName = sys.argv[1].rsplit("-",1)[0] + '-output1.txt'
    outputName = outputName.replace("Input","Output")

    
    problems(outputName,calBody,calReadings,empivot,optpivot)

def problems(outputName,calBody,calReadings,empivot,optpivot):
    """
        def problems, primary driver that runs the programs associated with each program, returns nothing 
        @param outputName, the file to be outputtted 
        @param calBody, data regarding the obejct
        @param calReadings, data regarding readings from the sensor
        @param empivot, EM markers data 
        @param optpitvot, optical markers on the probe data
    """

    # run the each question acquire the response
    cExepcted = q4.transformation(calBody,calReadings)
    pivCalReadings = q5.getCalibrationReadings(empivot)
    optCalReadings = q6.getCalibrationReadings(calBody,optpivot)

    # write each response to the output file
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
