import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:mariam83@ds125945.mlab.com:25945/recipes'

mongo = PyMongo(app)

@app.route('/')
@app.route('/all_recipes')
def all_recipes():
    return render_template("index.html",
    dishes=mongo.db.dishes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    allergens=mongo.db.allergens.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)
    
