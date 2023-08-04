from flask import render_template , request , redirect
from flask_app import app
from users import User

# from flask_app.controllers import users


if __name__ == '__main__':
    app.run(debug=True, port=5003)


@app.route('/')
def users():
    return render_template("users.html" , users = User.get(all))