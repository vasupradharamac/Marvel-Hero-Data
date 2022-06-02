import os
from ApiFunctions import *
from pynput import keyboard

publicKey = "e04fd41c572564f6ffe36dbfe1173aa3"
privateKey = "1c5e17de2e5c9f28d7559cd35541c6c6b8a30a02"
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
        choice = detectPress()

        if choice == "x":
            notClosed=False
        elif choice == "n":
            offset = min(offset+itemsPerPage, maxEntries-itemsPerPage)
        elif choice == "p":
            offset = max(offset-itemsPerPage, 0)
         