#Picture Poacher
#Code by: Grace Simonson, Charles Hebert, and Laura Sevilla
#Extra packages installed to Thonny: PIL (Python Image Library)

import os
from PIL import Image
import urllib.request

def saveImage(fileName, path): #saves image to file path specified (code by Grace)
    image = Image.open(fileName)
    image.save(path+'/'+fileName)

def saveImageUrl(url,outfileName): #returns a list of image urls found on website specified
    url1 = urllib.request.urlopen(url) #function code by Laura, Grace, and Charles
    urlList = []
    data = url1.read().decode('utf-8')
    with open(outfileName, 'w') as outFile:
        outFile.write(data)
    with open(outfileName, 'r') as outFile:
        for line in outFile:
            if '<img src="' in line:
                indx = line.find('img src="') + 9
                imgUrl = line[indx:line.find('"',indx,len(line))]
                if "http" in imgUrl:
                    urlList += [imgUrl]
    return urlList

url = input("Copy and paste the url of the website to scrape: \n")

myList = saveImageUrl(url, 'scrapedSite.txt')
acc = 0
for url in myList: #for loop iterates through url list, displays image, and saves image
    fileName = 'file' + str(acc) + url[url.rfind('.'):] #for loop code by Charles
    urllib.request.urlretrieve(url, fileName)
    
    im = Image.open(fileName)
    im.show()
    print("This file is called:", fileName)
    path = input("Put the full path of the folder you would like to save this image to:\n")
    saveImage(fileName, path)
    os.remove(fileName)
    acc += 1
    
print("You saved", len(myList), "files!") #success message