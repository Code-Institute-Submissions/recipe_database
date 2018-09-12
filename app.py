import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://<dbuser>:<dbpassword>@ds151282.mlab.com:51282/recipe_database'

mongo = PyMongo(app)

app.route('/')
def hello():
    return 'hello'
    
#app.route('/get_cusine')
#def get_cusines():
    #return render_template("index.html", 
    #cusine=mongo.db.cusine.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
            