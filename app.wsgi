import gevent.monkey
gevent.monkey.patch_thread()

import gevent_psycopg2
gevent_psycopg2.monkey_patch()

DSN = "postgresql+psycopg2://localhost/"
QUERY = "SELECT pg_sleep(5)"


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DSN)
DBSession = sessionmaker(bind=engine)


def application(env, start_response):
    start_response('200 OK', [])

    session = DBSession()
    session.execute(QUERY)

    return ['ok?\n']