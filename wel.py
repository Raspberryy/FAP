import os
import time

class b:
    purp = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yell = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    dick = '\033[1m'
    under = '\033[4m'

os.system("clear")
print ""
print "   " + b.under + b.red + "Fake Access Point" +b.white + "  by Raspebrry"
print ""
print "     Choose Vector: "
print "      1.) Explanation"
print "      2.) Start "
print "      3.) Exit "
print ""
fapv = input(" Enter Vector:  ")
if fapv == 1:
	os.system("clear")
	os.system("cat ./README.txt")
	time.sleep(5)
	execfile("./wel.py")	
elif fapv == 2:
	execfile("./airb.py")
elif fapv == 3:
	print ""

