from tinydb import TinyDB

from fixtures.data import FAKE_DATABASE

db = TinyDB('db.json')
db.truncate()
db.insert_multiple(FAKE_DATABASE)
