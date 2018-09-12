import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://admin:Tottenham18@ds151282.mlab.com:51282/recipe_database'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_cusines():
    return render_template("index.html", 
    recipes=mongo.db.recipes.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
            