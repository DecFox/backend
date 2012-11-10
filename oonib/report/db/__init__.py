from twisted.python import log
from twisted.python.threadpool import ThreadPool
from twisted.internet.defer import inlineCallbacks
from storm.twisted.transact import Transactor, transact
from storm.locals import *

from storm.uri import URI
from storm.databases.sqlite import SQLite

database = SQLite(URI('sqlite:///test.db'))

threadpool = ThreadPool(0, 10)
threadpool.start()
transactor = Transactor(threadpool)

def getStore():
    store = Store(database)
    return store

@inlineCallbacks
def create_tables():
    from oonib.report.models import models

    for x in models.__all__:
        query = getattr(models.__getattribute__(x), 'createQuery')
        try:
            yield transactor.run(create, query)
        except:
            log.msg("Failing in creating table for %s. Maybe it already exists?" % x)

create_tables()
