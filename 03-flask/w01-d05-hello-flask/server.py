from flask import Flask , render_template

app = Flask(__name__)


#http://127.0.0.1:5000/
#http://localhost:5000/
#(/)
@app.route('/')  #Route (localHost:5000+/)
#associated function
def index():
    return"Hello from Flask"


@app.route('/hi')
def hi():
    return"<h1>Hi</h1>"

@app.route('/circles')
def circles():
    return render_template("index.html")


@app.route('/hi/<username>')
def hi_user(username):
    print(username, "****************")
    return f"<h1>Hi {username}</h1>"







if __name__ =='__main__':
    app.run(debug=True)