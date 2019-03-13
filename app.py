import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:mariam83@ds125945.mlab.com:25945/recipes'

mongo = PyMongo(app)

@app.route('/')
def all_recipes():
    return render_template("index.html",
    recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")
doc= {}
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    data = request.form.items()
    all_ingred = [];
    all_steps = [];
    for k, v in data: 
        if k.startswith('ing'):
            doc["recipe_ingredients"]=all_ingred
            all_ingred.append(v)
        elif k.startswith('step'):
            doc["recipe_steps"]=all_steps
            all_steps.append(v)
        else:
            doc[k]= v  # error message appears for missing values; need an if else statement to handle error

    recipe = doc
    recipes=mongo.db.recipes 
    recipes.insert_one(recipe)
    return redirect(url_for('all_recipes'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)
    
