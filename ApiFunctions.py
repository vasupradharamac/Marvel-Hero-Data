# using global variables for testing
# we can easily implement storeCreds as a DB function

publicKey = None
privateKey = None
baseUrl = "http://gateway.marvel.com/v1/public"

def storeCreds(prKey, puKey):
    global privateKey, publicKey
    privateKey = prKey
    publicKey = puKey


import hashlib
from datetime import datetime
import time
import requests_cache

session = requests_cache.CachedSession('cacheData')

class Provider:

    def generateHashManual(self, puKey, prKey, ts):
        stringToHash = str(ts) + prKey + puKey
        reqHash = hashlib.md5(stringToHash.encode()).hexdigest()
        params = {'ts': str(ts), 'apikey': str(publicKey), 'hash': str(reqHash)}
        return params

    def generateHash(self):
        ts = datetime.now().time()
        return self.generateHashManual(puKey=publicKey, prKey= privateKey, ts=ts)

    def fetchData(self, url, extraparams):
        params = self.generateHash()
        params.update(extraparams)
        resp = session.get(baseUrl+url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            print("fetchError: API fetch request failed with code" + str(resp.status_code))
            return None


    def getCharacters(self, charName, limit =100):
        stTime = time.process_time()
        data = self.fetchData("/characters", extraparams={'limit': limit, 'nameStartsWith': charName})
        print("Found in "+ str(time.process_time()-stTime))
        
        if data != None:
            return data['data']['results']
        else:
            return []

    def registerCreds(self, prKey, puKey):
        storeCreds(prKey, puKey)

provider = Provider()