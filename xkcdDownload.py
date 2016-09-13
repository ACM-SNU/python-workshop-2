import requests, os, bs4, re

# Starting url
url = 'http://xkcd.com'
# Store comics in ./xkcd
# makedirs() ensures the folder exists
# exist_ok=True prevents function from throwing exception if folder already exists
# Python3: os.makedirs('xkcd', exist_ok=True)
os.makedirs('xkcd' ,exist_ok = True)

last_comic = 1732 - int(input("Enter number of comics: "))
# End loop when url ends with '#'
while not url.endswith(str(last_comic)+'/'):
	# Download the page
	print ('Downloading page %s...'% url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	# Find the URL of the comic image
	# <div id="comic"><img src=""></div>
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print ('Could not find comic image.')
	else:
		# Create regex to parse url below the comic (remember to escape the parentheses)
		pattern = re.compile(r'Image URL \(for hotlinking/embedding\): (.*)')
		# Pass pattern to BeautifulSoup's find() method
		comicUrl = soup.find(text=pattern)
		# Substitute with r'\1', the first group in parentheses: (.*)
		# Use strip to remove whitespace
		comicUrl = pattern.sub(r'\1', comicUrl).strip()
		# Download the image
		print ('Downloading the image %s...'% comicUrl)
		res = requests.get(comicUrl)
		res.raise_for_status()

		# Save the image to ./xkcd
		# comicUrl example: http://imgs.xkcd.com/comics/heartbleed_explanation.png
		# call os.path.basename() on it to return the last part of the url:
		# heartbleed_explanation.png (can use this as the filename of image when saving)
		# join() so program uses backslashes on Windows and forward clashes on OS X and Linux
		# call open() to open a new file in 'wb' "write binary" mode
		# to save downloaded files using Requests, loop over return value of the iter_content()
		# for loop writes chunks of the image data (max 100,000 bytes each) to the file
		# then close the file, the image is now saved your hard drive
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	# Get the Prev button's url
	# while loop begins the entire download process again for this comic
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print ('Done.')