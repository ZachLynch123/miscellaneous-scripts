import tweepy, os

def getStatus():
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

def tweetthis(type):
	if type == "text":
		print "Enter your tweet "+user.name
		tweet = getStatus()
		try:
			api.update_status(tweet)
		except Exception as e:
			print e
			return
	elif type == "pic":
		print "Enter pic path "+user.name
		pic = os.path.abspath(raw_input())
		print "Enter status "+user.name
		title = getStatus()
		try:
			api.update_with_media(pic, status=title)
		except Exception as e:
			print e
			return

	print "\n\nDONE!!"

def initialize():
	global api, auth, user
	ck = "egCBYLUaFz2O1uSkOaMztm6Ij" # consumer key
	cks = "EZgngtEU0o6617NAjYJ0P7fb5K73c8vjYrG2ss0cOxctrgxNh1" # consumer key SECRET
	at = "4308126313-2uN18LdAAD8qbiGDGSONze59lMkyaHN2S2Ary4a" # access token
	ats = "ZNXOHQvHZkPthDyNhzOgvAE8g02zRviJcteUnuDvdVQtH" # access token SECRET

	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)

	api = tweepy.API(auth)
	user = api.me()

def main():
	doit = int(raw_input("\n1. text\n2. picture\n"))
	initialize()
	if doit == 1:
		tweetthis("text")
		print "OK, Let's try again!"
		main()
	elif doit == 2:
		tweetthis("pic")
		print "OK, Let's try again!"
		main()

		

main()