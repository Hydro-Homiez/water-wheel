from flask import *  # Flask, render_template, request, redirect
import pyrebase

config = {
    "apiKey": "AIzaSyDoawNiKjMq535l5del-gYI7iuLlBTcYp8",
    "authDomain": "water-wheel-b5291.firebaseapp.com",
    "databaseURL": "https://water-wheel-b5291.firebaseio.com",
    "projectId": "water-wheel-b5291",
    "storageBucket": "water-wheel-b5291.appspot.com",
    "messagingSenderId": "849609847687",
    "appId": "1:849609847687:web:2eabfa8da2c8784ebb9922",
    "measurementId": "G-1K3FC27ZJ6"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
'''
#creates a table names and creates a column name with the row holland
#db.child("names").push({"name":"holland"})
#db.child("names").child("names").update({"name":"Ho"})

#users = db.child("names").child("name").get()
#print(users.key())

#this removes the whole table stated by the name in child
#db.child("names").remove()
'''

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        name = request.form['name']
        db.child("todo").push(name)
        todo = db.child("todo").get()
        to = todo.val()
        return render_template('overview.html', t=to.values())
    return render_template('overview.html')




if __name__ == '__main__':

    app.run(debug=True)


