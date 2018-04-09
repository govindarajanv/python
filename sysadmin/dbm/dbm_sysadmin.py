#Unix style key value store

import dbm

with dbm.open('/tmp/example.db', 'n') as db:
    db['key'] = 'value'
    db['OS'] = 'Linux'
    db['Cloud'] = 'AWS'

print(dbm.whichdb('/tmp/example.db'))
