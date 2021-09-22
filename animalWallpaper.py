import requests
import ctypes
from PIL import Image
from random import randint
from os import path
import GetAnimal

class AnimalWallpaper:
    def pickAnimalNumber(self):
        print("picking animal")
        
        return randint(0, len(self.urls)-1)

    def saveImage(self, path, img):
        # Opens the temp image file and writes the image to it
        with open(path, 'wb') as f:
            f.write(img.content)
        
    def resizeImg(self, width, height, imgPath, savePath):
        try:
            img = Image.open(imgPath)

            resizedImg = img.resize((width, height))
            
            resizedImg.save(savePath)

        except Exception as e:
            print("error encountered, exiting".title())
            print(e)
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
            print(e)
            exit(0)

    def updateLog(self, toWrite):
        #try:
        with open('history.txt', 'a') as f:
            f.write(toWrite + "\n")

        return True

    def findAbsoluteImgPath(self):
        absolutePath = path.realpath(__file__)

        absolutePath = absolutePath.split('\\')
        absolutePath = str(absolutePath.pop(len(absolutePath)-1))

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # The API Endpoint to retrieve the cat data supports images up to 1000x1000,
            # But if they add 1920x1080 support this won't need updating,
            # Requesting oversize images defaults to the max size
            #TODO: Insert native sizes into cat API call
        self.urls = {
            0 : "https://cataas.com/cat?json=true", # &width=" + str(self.width) + "&height=" + str(self.height)
            
            1 : "https://dog.ceo/api/breeds/image/random",

            2 : "https://randomfox.ca/floof/"
        }
        
        # Get the key of the animal chosen returned by pickAnimal()
            # This function only returns the key pair being used, hence [0]
        self.animalNumber = self.pickAnimalNumber()

        if self.animalNumber == 0:
            cat = GetAnimal.getCatImage(self.urls[self.animalNumber])
            self.saveImage('tempResize.png', cat)

        elif self.animalNumber == 1:
            dog = GetAnimal.getDogImage(self.urls[self.animalNumber])
            self.saveImage('tempResize.png', dog)

        elif self.animalNumber == 2:
            fox = GetAnimal.getFoxImage(self.urls[self.animalNumber])
            self.saveImage('tempResize.png', fox)

        else:
            print("Didn't pass lol")


if __name__ == "__main__":
    # Get the width and height of the user's
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)

    animalWallpaper = AnimalWallpaper(width, height)  

    animalWallpaper.resizeImg(width, height, r'temp.png', r'tempResize.png')

    #absoluteImgPath = animalWallpaper.findAbsoluteImgPath()

    animalWallpaper.changeWallpaper(r'C:\Users\marfx\Desktop\catWallpaper\tempResize.png') #TODO: Make an absolute path finder function