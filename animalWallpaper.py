import requests
import ctypes
from PIL import Image
from random import randint
from os import path
from sys import argv

class AnimalWallpaper:
    def pickAnimal(self, option):
        # The API Endpoint to retrieve the cat data supports images up to 1000x1000,
            # But if they add 1920x1080 support this won't need updating,
            # Requesting oversize images defaults to the max size
            #TODO: Insert native sizes into cat API call
        urls = {
            0 : {
            "cat" : "https://cataas.com/cat?json=true&width=1920&height=1080"
            },
            
            1 : {
            "dog" : "https://dog.ceo/api/breeds/image/random"
            },

            2 : {
            "fox" : "https://randomfox.ca/floof/"
            }
        }

        if option != "":
            return urls[2]
                
        # len() counts from 1
        return urls[randint(0, (len(urls) - 1))]

    def saveImage(self, path, img):
        # Opens the temp image file and writes the image to it
        with open(path, 'wb') as f:
            f.write(img.content)

    def getFoxImage(self):
        try:
            # Get request
            r = requests.get(self.url['fox'])

            foxImgUrl = r.json()['image']

            foxImg = requests.get(foxImgUrl)

            self.saveImage('temp.png', foxImg)

            return True

        except Exception as e:
            print("error encountered, exiting".title())
            print(e.Message)
            exit(0)

    def getCatImage(self):
        try:
            # Get request
            r = requests.get(self.url['cat'])

            # Appends the url of the cat image to the base
            catImgUrl = "https://cataas.com" + r.json()['url']

            # Cat Image Get Request
            catImg = requests.get(catImgUrl)

            self.saveImage('temp.png', catImg)

            return True

        except Exception as e:
            print("error encountered, exiting".title())
            print(e.Message)
            exit(0)

            return False

    def getDogImage(self):
        # Get request
        r = requests.get(self.url['dog'])

        dogImgUrl = r.json()['message']
        dogImg = requests.get(dogImgUrl)

        self.saveImage('temp.png', dogImg)

        return True
        

    def resizeImg(self, width, height, imgPath, savePath):
        try:
            img = Image.open(imgPath)

            resizedImg = img.resize((width, height))
            
            resizedImg.save(savePath)

        except Exception as e:
            print("error encountered, exiting".title())
            print(e.Message)
            exit(0)

    """
    imgPath must be an absolute path
    """
    def changeWallpaper(self, imgPath):
        if not path.isfile(imgPath):
            print("invalid image path, exiting".title())
            exit(0)
        
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, imgPath, 0)

        except Exception as e:
            print("error encountered, exiting".title())
            print(e.Message)
            exit(0)

    def updateLog(self):
        try:
            with open('history.txt', 'a') as f:
                f.write(self.url[self.animal] + "\n")

            return True

        except Exception as e:
            print("error encounted, exiting".title())
            print(e.Message)
            exit(0)

            return False

    def findAbsoluteImgPath():
        path = os.path.realpath()

        path = path.split('\\')
        path = str(path.pop(len(path)-1))


    def __init__(self, argv):
        if not argv[1] == "-f":
            self.url = self.pickAnimal("")

        else:
            self.url = self.pickAnimal("-f")

        # Get the key of the animal chosen returned by pickAnimal()
            # This function only returns the key pair being used, hence [0]
        self.animal = list(self.url.keys())[0]

        if self.animal.lower() == "cat":
            self.getCatImage()

        elif self.animal.lower() == "dog":
            self.getDogImage()


        elif self.animal.lower() == "fox":
            self.getFoxImage()


if __name__ == "__main__":
    animalWallpaper = AnimalWallpaper(argv)

    # Get the width and height of the user's
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)

    animalWallpaper.resizeImg(width, height, r'temp.png', r'tempResize.png')

    absoluteImgPath = animalWallpaper.findAbsoluteImgPath()

    animalWallpaper.changeWallpaper(r'C:\Users\marfx\Desktop\catWallpaper\tempResize.png') #TODO: Make an absolute path finder function


# https:\/\/randomfox.ca\/images\/69.jpg
# https://randomfox.ca//images//69.jpg