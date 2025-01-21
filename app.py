from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'New Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  },
{
  'id':4,
  'title':'Backend Engineer',
  'location':'San Francisco, USA',
  # 'salary':'$120,000'
}
]
@app.route('/')
def hello_world():
  # return "Hello World"
  return render_template('home.html',jobs=JOBS,name='Rajeev Veluthedathuparambil')

# Instead of returning html we can return some json (javascript object)
# @app.route("/jobs")
@app.route("/api/jobs")#api-Application programmable interface used to differentiate between html and non html pages, URL which does not return html but a structured data in the form of json which we programatically analyse
def list_jobs():
  return jsonify(JOBS)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# Cloud platform-render.com
