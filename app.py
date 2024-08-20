from flask import Flask, render_template, jsonify
from database import engine,load_jobs_from_db

app = Flask(__name__) 

@app.route("/")
def hello_World():
    return render_template("main.html", jobs=load_jobs_from_db())

@app.route("/jobs/")

@app.route("/api/jobs")
def jobs():
    return jsonify(load_jobs_from_db())


print(__name__)
if __name__ == "__main__":
    app.run(debug = True)