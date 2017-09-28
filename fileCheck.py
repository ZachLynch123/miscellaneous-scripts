import urllib
import webbrowser
def read_text():
	quotes = open('/Users/Zach/Desktop/pythonprojects/sampletext.txt')
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
	output = connection.read()
	if "true" in output:
		webbrowser.open('https://youtu.be/hpigjnKl7nI?t=2s')
	elif "false" in output:
		print("no curse words. :D")
	else:
		print("Failed to can file.")



read_text()
