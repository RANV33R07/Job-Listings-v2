from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(
            text("select * from jobs"))

        JOBS = []
        for row in result.all():
            JOBS.append(row)
    return JOBS


@app.route("/")
def hello_World():
    return render_template("main.html", jobs=load_jobs_from_db())


@app.route("/api/jobs")
def jobs():
    return jsonify(load_jobs_from_db())


print(__name__)
if __name__ == "__main__":
    app.run(debug = True)