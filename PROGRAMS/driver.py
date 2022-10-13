import sys
import q4 as q4
import q5 as q5
import q6 as q6
import test as test

def main():
    """
        Main, primary driver and takes input for files to test upon, or testing the general efficacy of the program itself 
        :return: None
    """

    # Placeholders for files
    calBody = None
    calReadings = None
    empivot = None
    optpivot = None

    # Enable test situation
    if (sys.argv[1] == 'test' and len(sys.argv) == 3):
        tolerance = float(sys.argv[2])
        test.test_operation(tolerance)
        sys.exit()
        

    # Enable the running of the program, parsing the inputs required to run the program, or otherwise, prevent user fro further running 
    if (len(sys.argv) == 5):
        # Assign
        calBody = sys.argv[1]
        calReadings = sys.argv[2]
        empivot = sys.argv[3]
        optpivot = sys.argv[4]
    else:
        raise("Insufficient Arguments")
    
    # Generate the output name for the given set of files

    # WARNING, BELOW NEEDS TO BE FIXED FOR GENERIC FILE CASE

    outputName = sys.argv[1].rsplit("-",1)[0] + '-output1.txt'
    #outputName = outputName.replace("Input","Output")

    # Run programs for problems 4,5,6, and output the result to a file
    problems(outputName,calBody,calReadings,empivot,optpivot)

def problems(outputName,calBody,calReadings,empivot,optpivot):
    """
         Primary driver that runs the programs associated with each problem, and outputs their results to a file
        :param outputName: Name of the file containing the results
        :param calBody: File that contains data regarding oboject calibration 
        :param calReadings: File that contains readings from the EM markers
        :param empivot: File that contains readings from EM markers  
        :param optpivot: File that contains from readings Optical Markers 

        :type outName: str
        :type calBody: str
        :type calreadings: str
        :type empivot: str
        :type optpivot: str

        :return: None
    """
    # run the each question acquire the response
    cExepcted = q4.getCExepcted(calBody,calReadings)
    pivCalReadings = q5.getRelativePosition(empivot)
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
