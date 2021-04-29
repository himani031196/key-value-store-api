import sqlite3

class KeyValueStore():
    def __init__(self):
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS kv (key text unique, value text)")

    def close(self):
        self.conn.commit()
        self.conn.close()

    def iterkeys(self):
        c = self.conn.cursor()
        for row in c.execute('SELECT key FROM kv'):
            yield row[0]

    def getitem(self, key):
        item = self.conn.execute('SELECT value FROM kv WHERE key = ?', (key,)).fetchone()
        if item is None:
            raise KeyError(key)
        return item[0]

    def setitem(self, key, value):
        self.conn.execute('REPLACE INTO kv (key, value) VALUES (?,?)', (key, value))
