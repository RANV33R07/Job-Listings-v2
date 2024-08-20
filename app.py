from flask import Flask, render_template, jsonify
from database import engine,load_jobs_from_db,load_job_from_db

app = Flask(__name__) 

@app.route("/")
def hello_World():
    return render_template("main.html", jobs=load_jobs_from_db())

@app.route("/jobs/")
def get_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/jobs/<id>")
def get_job(id):
    job = load_job_from_db(id)
    if (job == None) : return jsonify("No record Found" )
    return jsonify(job)

print(__name__)
if __name__ == "__main__":
    app.run(debug = True)