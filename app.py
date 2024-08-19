from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS=[
    {
        "id":1,
        "title":"Data Analyst",
        "location":"Bengluru, India",
        "salary":"RS. 20,00,000"
    },
    {
        "id":2,
        "title":"Machine Learning Engineer",
        "location":"New York City, USA",
        "salary":"RS. 30,00,000"
    },
    {
        "id":3,
        "title":"Applied Data Scientist",
        "location":"San Fransisco, USA",
        "salary":"$120,000"
    },
    {
        "id":4,
        "title":"Frontend Engineer",
        "location":"Dholakpur, India",
    }
]

@app.route("/")
def hello_World():
    return render_template("main.html" , jobs = JOBS,name="Ranveer Singh")

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
    app.run(debug = True)