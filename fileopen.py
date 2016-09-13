with open("blahblah.txt") as myFile:
    for lines in myFile:
        print (lines) # or do some other thing with the line...


with open('newfile.txt', 'a') as the_file:
	the_file.write('Hello from the other side\n')
