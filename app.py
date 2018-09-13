import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://admin:Tottenham18@ds151282.mlab.com:51282/recipe_database'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("index.html", 
    recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
    cusine=mongo.db.cusine.find(),
    difficulty=mongo.db.difficulty.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id" : ObjectId(recipe_id)})
    all_cusines = mongo.db.cusine.find()
    all_difficulties = mongo.db.difficulty.find()
    return render_template('edit_recipe.html', index=the_recipe, cusine=all_cusines, difficulty=all_difficulties)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
            