import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://admin:Tottenham18@ds151282.mlab.com:51282/recipe_database'

mongo = PyMongo(app)



@app.route('/', methods=["GET", "POST"])
def index():
    """
    the backend for the username sign up page, the username will be added to users.txt
    then redirect to the page which displays all the recipes
    
    """
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.write(request.form["username"] + "/n")
        return redirect(url_for('get_recipes'))
    return render_template("index.html")



@app.route('/loggedin')
def loggedin():
    """
    simple app route to render the main page
    """
    return render_template('loggedin.html')
    
    

@app.route('/logout')
def logout():
    """
    a simple logout feature when the user clicks on logout they will be redirect to the 
    page to chose their username
    """
    return redirect(url_for('index'))
    
    

@app.route('/get_recipes', methods=["POST", "GET"])
def get_recipes():
    """
    this feature fetches all the recipes stored in my mongo database on mlabs 
    """
    return render_template("loggedin.html", 
                            recipes=mongo.db.recipes.find())
    
    

@app.route('/add_recipe')
def add_recipe():
    """
    backend code which will help to find cusine and difficulty from the database
    """
    return render_template('add_recipe.html',
                            cusine=mongo.db.cusine.find(),
                            difficulty=mongo.db.difficulty.find())
    
 

@app.route('/insert_recipe', methods=['POST', 'GET'])
def insert_recipe():
    """
    this function send the data entered by the user to the database on mlab
    """
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
    

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
    it will fetch the id for what recipe the user has decided to edit and add the existing data
    to the fields in the form
    """
    the_recipe = mongo.db.recipes.find_one({"_id" : ObjectId(recipe_id)})
    all_cusines = mongo.db.cusine.find()
    all_difficulties = mongo.db.difficulty.find()
    return render_template('edit_recipe.html', 
                            index=the_recipe, 
                            cusine=all_cusines, 
                            difficulty=all_difficulties)
    
    

@app.route('/update_recipe/<recipe_id>, methods=["POST"]')
def update_recipe(recipe_id):
    """
    this will post the updated changes made by the user and make the changes in mlab
    """
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
    """
    this function simplys deletes the chosen recipe from the database via the id
    """
    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    


@app.route('/chinese_filter')
def chinese_filter():
    """
    All the app route for the filter function, so i will only show
    recipes with that matching cuisine
    """
    return render_template("chinese.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Chinese'}))
    
    
@app.route('/english_filter')
def english_filter():
    return render_template("english.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'English'}))  
    
    
@app.route('/italian_filter')
def italian_filter():
    return render_template("italian.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Italian'}))
    
    
@app.route('/indian_filter')
def indian_filter():
    return render_template("indian.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Indian'}))
    
    
@app.route('/mexican_filter')
def mexican_filter():
    return render_template("mexican.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Mexican'}))
    
    
@app.route('/spanish_filter')
def spanish_filter():
    return render_template("spanish.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Spanish'}))
    
    
@app.route('/thai_filter')
def thai_filter():
    return render_template("thai.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Thai'}))
    
    
@app.route('/other_filter')
def other_filter():
    return render_template("other.html",
                            recipes=mongo.db.recipes.find({'cusine_name' : 'Other'}))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
            