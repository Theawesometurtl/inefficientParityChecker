

def createUselessParityChecker(length):
    f = open("ParityChecker.py", "w+")
    f.write("def IsEven(num):\n")
    for i in range(1, length + 1, 2):
        print(i)
        f.write("\tif num == %s: return False\n" % (i))
        f.write("\tif num == %s: return True\n" % (i+1))
    f.close()
createUselessParityChecker(100000)

