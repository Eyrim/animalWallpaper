import requests

def getCatImage(url):
    print("Gettinc cat")
    response = requests.get(url)

    catImgUrl = "htttps://cataas.com" + response.json()['url']

    catImg = requests.get(catImgUrl)

    return catImg


def getFoxImage(url):
    print("Getting fox")
    response = requests.get(url)

    foxImgUrl = response.json()['image']

    foxImg = requests.get(foxImgUrl)

    return foxImg


def getDogImage(url):
    print("Getting dog")
    response = requests.get(url)

    dogImgUrl = response.json()['message']

    dogImg = requests.get(dogImgUrl)

    return dogImg