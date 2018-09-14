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
    
@app.route('/update_recipe/<recipe_id>, methods=["POST"]')
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get['recipe_name'],
        'cusine_name':request.form.get['cusine_name'],
        'time_details':request.form.get['time_details'],
        'serves_details':request.form.get['serves_details'],
        'difficulty_selector':request.form.get['difficulty_selector'],
        'ingredients_details':request.form.get['ingredients_details'],
        'instructions_details':request.form.get['instructions_details']
    })
    return redirect(url_for('get_recipes'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
@app.route('/signup')
def signup():
    return render_template('signup.html')
    
@app.route('/insert_signup', methods=['POST'])
def insert_signup():
    usernames = mongo.db.usernames
    usernames.insert_one(request.form.to_dict())
    return redirect(url_for('signup'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
            