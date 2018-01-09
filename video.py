import requests

def download_file(url):
	local_filename = url.split('/')[-1]
	# NOTE the stream=True parameter
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				#f.flush() commented by recommendation from J.F.Sebastian

	return local_filename

#url = input("Please paste the source of the file: ")
#remoded = url.replace(".","")
#print(url)
download_file("https://sdbcdn.net/upload/2018/01/01/20180101041749-39255062.mp4")
# becca bae

# https://sdbcdn.net/upload/2017/12/31/20171231222227-65f5d1f0.mp4
# https://sdbcdn.net/upload/2017/12/31/20171231210002-f687a33c.mp4
# https://sdbcdn.net/upload/2017/12/31/20171231220254-e58bc64e.mp4
# https://sdbcdn.net/upload/2017/12/31/20171231213908-49d307e7.mp4 last
# http://xhamster.com/xembed.php?video=7473428

