import time
delay = 0.2
repeats = 50
for i in range(repeats):
    with open('sudowoodoMed.txt') as woodoFile:
        x = ""
        for line in woodoFile:
            x += line + "\t"  
        print(x)    
        woodoFile.close()
    time.sleep(delay)
    with open('sudowoodoMed.txt') as woodoFile:
        x = ""
        for line2 in woodoFile:
            reservedLine = line2[::-1]
            x += reservedLine + "\t"
        print(x)
    time.sleep(delay)