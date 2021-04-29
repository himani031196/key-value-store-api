from app import app
import json
import unittest
from unittest.mock import patch
import sqlite3
from keyvalueapi import KeyValueApi


class KeyValueApiTest(unittest.TestCase):

    #Setups an environment for tests to be executed 
    def setUp(self):
        self.api = KeyValueApi()
        self.api.set_items("abc-1", "verified")
        self.api.set_items("abc-2", "verified")
        self.api.set_items("xyz-1", "verified")

    #Testing the home Page loads
    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertEqual(response.status_code, 200)

    # #Testing the home Page loads
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertTrue(b'This is an implementation of Key Value Store' in response.data)

    #Testing the key value set api 
    def test_set_functionality(self):
        tester =  app.test_client(self)
        data = {"key":"abc-2","value":"one"}
        response = tester.post("/set", data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data Added Successfully', response.data)
    
    #Testing the Key Value Get API

    def test_get_key_api(self):
        tester =  app.test_client(self)
        data = {"key":"abc-2","value":"one"}
        tester.post("/set", data=json.dumps(data))
        uri = "/get?key=" + "abc-2"
        response = tester.get(uri)
        self.assertEqual( b'"one"\n', response.data)

    def test_get_key_module(self):
        key = "abc-1"
        response = self.api.get_key_value(key)
        self.assertEqual("verified", response)

    #Testing the Key Value Prefix Functionality
    def test_prefix_functionality(self):
        neg_response = self.api.search_prefix_in_key("pqr")
        self.assertListEqual([], neg_response)

        pos_response = self.api.search_prefix_in_key("abc")
        self.assertListEqual(pos_response, ["abc-1", "abc-2"] )

    #Testing the Key Value Prefix Functionality
    def test_suffix_functionality(self):
        neg_response = self.api.search_suffix_in_key("-4")
        self.assertListEqual([], neg_response)

        pos_response = self.api.search_suffix_in_key("-1")
        self.assertListEqual(pos_response, ["abc-1", "xyz-1"] )

        
if __name__ == "__main__":
    unittest.main()
