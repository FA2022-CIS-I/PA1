


def main():
    file = open("autoRun.bat","w")
    for i in range(0,7):
        letter = chr(ord('a')+i)
        file.write('python driver.py Input\pa1-debug-{0}-calbody.txt Input\pa1-debug-{0}-calreadings.txt Input\pa1-debug-{0}-empivot.txt Input\pa1-debug-{0}-optpivot.txt\n echo \"COMPLETE\"\n'.format(letter))

    file.close()
    file = open("autoTest.bat","w")
    for i in range(0,7):
        letter = chr(ord('a')+i)
        file.write('echo TEST LETTER{0}\npython comparison.py Input\pa1-debug-{0}-output1.txt Output\pa1-debug-{0}-output1.txt\n'.format(letter))
    file.close()



if __name__ == "__main__":
    main()
