import unittest
from ApiFunctions import *
from hashlib import md5

class TestClass(unittest.TestCase):

    def test_AuthRegister(self):
        provider.registerCreds("dumPrKey","dumPvKey")
        self.assertEqual(privateKey,"dumPrKey","Private Key store error")
        self.assertEqual(publicKey,"dumPvKey","Public Key store error")

    def test_hash_generation(self):
        provider.registerCreds("af62d9215a85043fdfd1fc1a53a48334","c1bffc25b2605412fe272d32e235575225847127")
        params=provider.generateHashManual(publicKey,privateKey,1)
        print(publicKey,privateKey)
        toHash="1"+privateKey+publicKey
        self.assertEqual(params['hash'],md5(toHash.encode()).hexdigest()
                         ,"Hash generated mismatch")

    def test_fetch_data(self):
        data=provider.fetchData("/characters",{})
        self.assertIsNotNone(data,"Fetch returns None")


if __name__ == '__main__':
    unittest.main()