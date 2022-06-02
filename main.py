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

        
        