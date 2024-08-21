import sqlalchemy
from sqlalchemy import create_engine, text
import os

<<<<<<< HEAD
db_connection_string = "mysql+pymysql://2MV7kAJ8u835cqi.root:qOjWOWxOhLy0Zi86@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/test?charset=utf8mb4" 
=======
db_connection_string = os.environ['DB_CONNECTION_STRING']
>>>>>>> 53216c10019ca0979b6025ebd1e21b84e7c8134b

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/isrgrootx1.pem",
                       }})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(
            text("SELECT * FROM jobs")
        )
        jobs = [dict(row._mapping) for row in result]
    return jobs

def load_job_from_db(job_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"), {"id": job_id}
        )
    rows = result.all()
    if (len(rows) == 0) : return None
    else : return dict(rows[0]._mapping)
<<<<<<< HEAD


def add_applications_to_db(id, data):
    with engine.begin() as conn:
        query = text("""
            INSERT INTO applications 
            (job_id, full_name, email, linkedin, education, experience, resume) 
            VALUES (:job_id, :full_name, :email, :linkedin, :education, :experience, :resume)
        """)
        conn.execute(query, {
            "job_id": id,
            "full_name": data['Name'],
            "email": data["Email"],
            "linkedin": data["linkedin"],
            "education": data["education"],
            "experience": data["experience"],
            "resume": data["resume"]
        })
        print("Data inserted with transaction block.")

=======
>>>>>>> 53216c10019ca0979b6025ebd1e21b84e7c8134b
