import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:mariam83@ds125945.mlab.com:25945/recipes'
app.config['SECRET_KEY'] = os.urandom(24) 
mongo = PyMongo(app)


""" Load user login/registration page """
@app.route('/')
def index():
    return render_template("index.html")

""" Check data submitted via Registration form """
@app.route('/register', methods=['POST'])
def register():
    users = mongo.db.users
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({'username': username})
    if registered is None:
        users.insert_one({
            'username': username,
            'fullname': fullname,
            'password': password
        })
        success = True
        return render_template('index.html', success = success)
    success = False    
    return render_template('index.html', success = success)
        
""" Check data submitted via Login form """
@app.route('/logout', methods=['POST'])
def login():
    users = mongo.db.users
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({'username': username, 'password': password})
    if registered is not None:
        session['username'] = username
        login = True
        return redirect(url_for('all_recipes'))
    login = False    
    return render_template('index.html', login=login)

""" Redirects guest users to website home page """
@app.route('/guest_user')
def guest_user():
    return redirect(url_for('all_recipes'))

""" Logout a user by removing username from session """
@app.route('/login')
def logout():
    session.clear()
    return render_template('index.html')

""" Home page displaying all uploaded recipes """
@app.route('/all_recipes')
def all_recipes():
    recipes=mongo.db.recipes.find()
    cuisines =  mongo.db.cuisines.find()
    dishes=mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    total_recipes=recipes.count()
    return render_template("home.html", recipes=recipes, dishes=dishes,
                            cuisines=cuisines, users=users, total_recipes=total_recipes, allergens=allergens)
 
""" Displays detail view of a recipe """    
@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    recipes=mongo.db.recipes
    cuisines =  mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template("recipe.html",
                        recipe = recipes.find_one({'_id': ObjectId(recipe_id),'recipe_title': recipe_title}),
                        cuisines=cuisines, dishes=dishes, allergens=allergens, users=users)

""" Display form to add a recipe """ 
@app.route('/add_recipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    dishes=mongo.db.dishes.find()
    cuisines=mongo.db.cuisines.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template("addrecipe.html", cuisines=cuisines, dishes=dishes, 
                            recipes=recipes, allergens=allergens, users=users)

""" Display form to edit the recipe """
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes=mongo.db.recipes.find()
    dishes=mongo.db.dishes.find()
    cuisines=mongo.db.cuisines.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template('editrecipe.html',  
                        recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}),
                        cuisines = cuisines, dishes = dishes, allergens = allergens, users=users)

""" Send form data to update recipe in MongoDB """
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe =  mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_author_name': session['username'],
        'recipe_title':request.form.get('recipe_title'),
        'recipe_short_description':request.form.get('recipe_short_description'),
        'recipe_image_url': request.form.get('recipe_image_url'),
        'cuisine_name': request.form.get('cuisine_name'),
        'dish_type':request.form.get('dish_type'),
        'allergen_name':request.form.getlist('allergen_name'),
        'recipe_prep_time':request.form.get('recipe_prep_time'),
        'recipe_cook_time':request.form.get('recipe_cook_time'),
        'total_time':request.form.get('total_time'),
        'recipe_serves':request.form.get('recipe_serves'),
        'recipe_ingredients':request.form.getlist('ingred'),
        'recipe_steps':request.form.getlist('steps'),
    })
    return redirect(url_for('all_recipes'))
  
""" Add new recipe data to MongoDB """   
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    doc ={'recipe_author_name': session['username'], "upvotes": 0}
    data = request.form.items()
    all_ingred = request.form.getlist('ingred')
    all_steps = request.form.getlist('steps')
    all_allergens = request.form.getlist("allergen_name")
    for k, v in data: 
        if k == "ingred":
            doc["recipe_ingredients"]=all_ingred
        elif k == "steps":
            doc["recipe_steps"]=all_steps
        elif k == "allergen_name":
            doc["allergen_name"] = all_allergens
        else:
            doc[k]= v  

    new_recipe = doc
    the_recipe=mongo.db.recipes
    the_recipe.insert_one(new_recipe)
    return redirect(url_for('all_recipes'))

""" Removes a recipe from MongoDB """
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes')) 

""" Displays all cuisines in MongoDB """
@app.route('/all_cuisines')
def all_cuisines():
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    return render_template("allcuisines.html", cuisines=cuisines, dishes=dishes,
                            users=users, allergens=allergens)

""" Displays form to add new cuisine """
@app.route('/add_cuisine')
def add_cuisine():
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    return render_template("addcuisine.html", cuisines=cuisines, dishes=dishes,
                            users=users, allergens=allergens)

""" Adds new cuisine to MongoDB """
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine = request.form.to_dict()
    cuisines=mongo.db.cuisines
    cuisines.insert_one(cuisine)
    return redirect(url_for('all_cuisines'))
 
""" Displays form to edit cuisine """    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    cuisine=mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template('editcuisine.html', cuisine=cuisine)    

""" Send form data to update cuisine in MongoDB """ 
@app.route('/update_cuisine/<cuisine_id>', methods=["POST"])
def update_cuisine(cuisine_id):
    cuisine =  mongo.db.cuisines
    cuisine.update({'_id': ObjectId(cuisine_id)},
                   {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('all_cuisines'))  

""" Removes a cuisine from MongoDB """
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    cuisine =  mongo.db.cuisines
    cuisine.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('all_cuisines'))       

""" Displays all dishes existing in MongoDB """ 
@app.route('/all_dishes')
def all_dishes():
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    return render_template("alldishes.html", cuisines=cuisines, dishes=dishes,
                            users=users, allergens=allergens)

""" Displays form to add a new dish """
@app.route('/add_dish')
def add_dish():
    dishes=mongo.db.dishes.find()
    return render_template("adddish.html", dishes=dishes)

""" Adds a new dish to MongoDB """
@app.route('/insert_dish', methods=['POST'])
def insert_dish():
    dish = request.form.to_dict()
    dishes=mongo.db.dishes
    dishes.insert_one(dish)
    return redirect(url_for('all_dishes'))
 
""" Displays form to edit a dish """    
@app.route('/edit_dish/<dish_id>')
def edit_dish(dish_id):
    dish =  mongo.db.dishes
    dish.find_one({"_id": ObjectId(dish_id)})
    return render_template('editdish.html', dish=dish)    

""" Send form data to update the dish in MongoDB """ 
@app.route('/update_dish/<dish_id>', methods=["POST"])
def update_dish(dish_id):
    dish =  mongo.db.dishes
    dish.update({'_id': ObjectId(dish_id)},
                {'dish_type': request.form.get('dish_type')})
    return redirect(url_for('all_dishes'))  

""" Remove the dish in MongoDB """ 
@app.route('/delete_dish/<dish_id>')
def delete_dish(dish_id):
    the_dish =  mongo.db.dishes
    the_dish.remove({'_id': ObjectId(dish_id)})
    return redirect(url_for('all_dishes')) 


""" Search by Cuisine """  
@app.route('/search_cuisine/<cuisine_name>')
def search_cuisine(cuisine_name):
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    cuisine_result = recipes.find({'cuisine_name': cuisine_name})
    cuisine_count = cuisine_result.count()
    return render_template('searchcuisine.html', result = cuisine_result, cuisine_name = cuisine_name,
                            count = cuisine_count, cuisines=cuisines, dishes=dishes, users=users, allergens=allergens)

""" Search by dish types """
@app.route('/search_dish/<dish_type>')
def search_dish(dish_type):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    dish_result = recipes.find({'dish_type': dish_type})
    dish_count = dish_result.count()
    return render_template('searchdish.html', result = dish_result, dish_type=dish_type,
                            count = dish_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens) 

""" Search by authors """
@app.route('/search_author/<author_name>')
def search_author(author_name):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    author_result = recipes.find({'recipe_author_name': author_name})
    author_count = author_result.count()
    return render_template('searchauthor.html', result = author_result, author_name=author_name,
                            count = author_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)

""" Search by allergens """
@app.route('/search_allergen/<allergen_name>')
def search_allergen(allergen_name):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    allergen_result = recipes.find({'allergen_name':{'$not': {'$eq': allergen_name}}})
    allergen_count = allergen_result.count()
    return render_template('searchallergen.html', result = allergen_result, allergen_name=allergen_name, 
                            count = allergen_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)


""" Search by keyword """
@app.route('/search_keyword', methods=['POST'])
def search_keyword():
    keyword = request.form.get('keyword')
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    recipes.create_index([
         ("recipe_title", "text"),
         ("recipe_ingredients", "text"),
         ("cuisine_name", "text"),
         ("dish_type", "text"),
         ("recipe_author_name", "text")
       ])
    keyword_result = recipes.find({"$text": {"$search": keyword}})
    keyword_count = keyword_result.count()
    return render_template('searchkeyword.html', result = keyword_result, keyword=keyword, 
                            count = keyword_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)

""" Function to upvote a recipe """
@app.route('/recipe_upvotes/<recipe_id>', methods=["POST"])
def recipe_upvotes(recipe_id):
    recipes =  mongo.db.recipes
    recipes.update(
        {'_id': ObjectId(recipe_id)},
        {'$inc':{"upvotes": 1}})
    return redirect(url_for('all_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)
    
