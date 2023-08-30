from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Cook' ,
    'location' : 'NeverEnd Ln, NJ',
    'salary' : '$200,000'
  },
  {
    'id' : 2,
    'title' : 'Cleaner' ,
    'location' : 'Somewhere Over the Rainbow',
    'salary' : '$500,000'
  },
  {
    'id' : 3,
    'title' : 'House Manager' ,
    'location' : 'Everywhere, USA',

  },
    {
    'id' : 4,
    'title' : 'Rubber Ducky' ,
    'location' : 'Rub Me Everywhere Lane, NJ',
    'salary' : '$900,000'
  }
]

@app.route("/")
def hello_angel():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  