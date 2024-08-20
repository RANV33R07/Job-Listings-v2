import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/isrgrootx1.pem",
                       }})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(
            text("select * from jobs"))

        JOBS = []
        for row in result.all():
            JOBS.append(row)
    return JOBS