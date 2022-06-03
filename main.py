import os
import sys

from ApiFunctions import *
from pynput import keyboard
from apiKeys import publicKey,privateKey
import math



baseUrl="http://gateway.marvel.com/v1/public"

def detectPress():
    with keyboard.Events() as events:
        event = events.get(10**6)
        return str(event.key)[1]


def doPagination(data,itemsPerPage=10):
    notClosed=True
    offset=0
    endPage=itemsPerPage
    curPageNo=1
    maxEntries=len(data)
    lastPage=math.floor(maxEntries/itemsPerPage)+1

    while notClosed and maxEntries>0:
        os.system('cls')
        curPageNo=math.floor(offset/itemsPerPage)+1
        print("Page Number : ",curPageNo)
        for i in range(offset,endPage):
            indentSpace=" "*len(str(i))
            hero=data[i]
            print("\n")
            print("*"*100)
            print(f"{i+1} :Name : "+hero['name'])
            if hero.get('thumbnail'):
                print(f"{indentSpace} ImageUrl : "+hero['thumbnail']['path'])
            if hero.get('description'):
                if hero['description']=="":
                    hero['description']=f"{indentSpace} No short Description"
                print(f"{indentSpace} Description : "+hero['description'][:100])
            print("*"*100)
            print("\n")
        # choice=input("X-> close results, N-> next page ,P-> Previous page")
        opNeeded=True
        while(opNeeded):
            print("X-> close results, N-> next page ,P-> Previous page")
            choice=detectPress()
            if choice=="x":
                notClosed=False
            elif choice=="n":
                if curPageNo==lastPage:
                    print("No More Pages After this")
                    input("press to continue")
                    continue
                offset+=itemsPerPage
            elif choice=="p":
                if curPageNo==1:
                    print("No More Pages before this")
                    input("press to continue")
                    continue
                print("ehr")
                offset=max(offset-itemsPerPage,0)
            opNeeded=False

        endPage=min(offset+itemsPerPage,maxEntries)
        print(endPage,offset)




if __name__ == '__main__':
    print("Type X as query to quit")
    while(True):
        print("*"*20+"Main Menu"+"*"*20)
        print("Query : ",end="")
        query=input()
        if query=="x":
            print("REPL client terminated")
            sys.exit(0)
        provider.registerCreds(prKey=privateKey,puKey=publicKey)
        heroes=provider.getResults(query)
        print("Found "+str(len(heroes))+" matching marvel heroes")
        doPagination(heroes)





