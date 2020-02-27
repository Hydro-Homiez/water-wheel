from flask import *  # Flask, render_template, request, redirect
import pyrebase
import json

with open('config.json') as config_file:
    config = json.load(config_file)

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
       # item_name = request.form['item']

        db.child("category").push(name)
        category = db.child("category").get()
        cate = category.val()
# Trying to make another table?
       # db.child("item").push(item_name)

        return render_template('overview.html', t=cate.values())
    return render_template('overview.html')




if __name__ == '__main__':

    app.run(debug=True)


