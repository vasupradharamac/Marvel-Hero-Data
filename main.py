import os
from ApiFunctions import *
from pynput import keyboard
from apiKeys import *

publicKey = publicKey
privateKey = privateKey
baseUrl = "http://gateway.marvel.com/v1/public"

def detectPress():
    with keyboard.Events() as events:
        event = events.get(10**6)
        return str(event.key)[1]

def doPagination(data, itemsPerPage=10):
    notClosed = True
    offset = 0
    maxEntries = len(data)
    while notClosed and maxEntries>0:
        for i in range(offset, min(offset+itemsPerPage, maxEntries)):
            hero = data[i]
            print("Name :" +hero['name'])
            if hero.get('thumbnail'):
                print("ImageUrl :" +hero['thumbnail']['path'])
            if hero.get('description'):
                if hero['description']=="":
                    hero['description'] = "No short description"
                print("Description: " +hero['description'][:50])
            print("*"*10)
        print("X -> Close results, N -> Next page, P -> Previous page")
        choice = input()

        if choice == "x":
            notClosed=False
        elif choice == "n":
            offset = min(offset+itemsPerPage, maxEntries-itemsPerPage)
        elif choice == "p":
            offset = max(offset-itemsPerPage, 0)
    

if __name__ == "__main__":
    while(True):
        print("*"*20+"Main Menu"+"*"*20)
        print("Enter query: ", end="")
        query=input()
        provider.registerCreds(prKey=privateKey, puKey=publicKey)
        heroes = provider.getCharacters(query)
        print("Found "+ str(len(heroes))+ " matching marvel heroes")
        doPagination(heroes)
         
