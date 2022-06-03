publicKey=None
privateKey=None
baseUrl="http://gateway.marvel.com/v1/public"

def storeCreds(prKey,puKey):
    global privateKey,publicKey
    privateKey=prKey
    publicKey=puKey


import hashlib
from datetime import datetime
import time
import requests_cache

session=requests_cache.CachedSession('cacheData')

class Provider:

    def __init__(self):
        self.cacheDict={}

    def generateHashManual(self,puKey,prKey,ts):

        stringToHash=str(ts)+prKey+puKey
        reqHash=hashlib.md5(stringToHash.encode()).hexdigest()
        params={'ts':str(ts),'apikey':str(publicKey),'hash':str(reqHash)}
        # print(params)
        return params

    def generateHash(self):
        ts=datetime.now().time()
        return self.generateHashManual(puKey=publicKey,prKey=privateKey,ts=ts)

    def fetchData(self,url,extraParams):
        params=self.generateHash()
        params.update(extraParams)
        resp=session.get(baseUrl+url,params=params)
        if resp.status_code==200:
            return resp.json()
        else:
            print("fetchError : API fecth request failed with code"+str(resp.status_code))
            return None

    def getCharacters(self,charName,limit=100):

        data=self.fetchData("/characters",
                       extraParams={'limit':limit,'nameStartsWith':charName})
        if data!=None:
            return data['data']['results']
        else:
            return []

    def getResults(self,queryString):
        pass

    def registerCreds(self,prKey,puKey):
        storeCreds(prKey,puKey)

    def getResults(self,query):
        stTime=time.process_time()
        if query in self.cacheDict:
            print("Found in "+str(time.process_time()-stTime))
            return self.cacheDict[query]
        else:
            res=self.getCharacters(query)
            print("Found in "+str(time.process_time()-stTime))
            self.cacheDict[query]=res
            return res

provider=Provider()