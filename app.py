from flask import Flask, render_template, jsonify,request
from database import engine,load_jobs_from_db,load_job_from_db,add_applications_to_db

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
    return render_template("jobpage.html" , j=job)

@app.route("/jobs/<id>/apply" , methods = ["post"])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_applications_to_db(id , data)
    return render_template("application_submitted.html",data = data,job = job)

    

if __name__ == "__main__":
    app.run(debug = True)