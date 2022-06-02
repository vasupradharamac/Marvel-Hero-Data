import unittest
from ApiFunctions import *
from hashlib import md5

class TestClass(unittest, TestCase):

    def test_AuthRegister(self):
        provider.registerCreds("dumPrKey", "dumPuKey")
        self.assertEqual(privateKey,"dumPrKey","Private Key store error")
        self.assertEqual(publicKey,"dumPuKey","Public Key store error")

    def test_hash_generation(self):
        provider.registerCreds("e04fd41c572564f6ffe36dbfe1173aa3", "1c5e17de2e5c9f28d7559cd35541c6c6b8a30a02")
        params = provider.generateHashManual(publicKey, privateKey, 1)
        print(publicKey, privateKey)
        toHash = "1" +privateKey+publicKey
        self.assertEqual(params['hash'], md5(toHash.encode()).hexdigest(), "Hash generated mismatch")

    def test_fetch_data(self):
        data = provider.fetchData("/characters", {})
        self.assertIsNotNone(data, "Fetch returns None")

if __name__ == '__main__':
    unittest.main()
