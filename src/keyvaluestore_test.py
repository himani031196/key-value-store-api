import json
import unittest
import sqlite3
from keyvaluestore import KeyValueStore

class KeyValueStoreTest(unittest.TestCase):

    #Setups an environment for tests to be executed 
    def setUp(self):
        self.db = KeyValueStore()
        self.db.conn.execute('REPLACE INTO kv (key, value) VALUES (?,?)', ("abc-1", "verified"))
        self.db.conn.commit()

    #test the get functionality of the database 
    def test_get_items(self):
        response = self.db.getitem("abc-1")
        value = 'verified'
        self.assertEquals(value, response)
        self.assertIsNotNone(value)
    
    #Tests the set functionality of the database 
    def test_set_items(self):
        self.db.setitem("abc-2", "verified")

    #Tears Down the SetUp environment    
    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()

    
