import webbrowser
import time
num_breaks = 3
counter = 0
print ("This program started at "+time.ctime())
while (counter < num_breaks):
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=jB809oiPE1c&list=WL&index=26")
	counter = counter + 1
print ("This program stopped at "+ time.ctime())