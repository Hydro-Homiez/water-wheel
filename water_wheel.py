from flask import *  # Flask, render_template, request, redirect
import pyrebase

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


