from tinydb import TinyDB

from fixtures.data import FAKE_DATABASE

db = TinyDB('db.json')
db.truncate()

for template in FAKE_DATABASE:
    db.insert(template)
