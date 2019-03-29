import os
import math
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
            'password': password,
            'upvoted_recipes':[],
            'fav_recipes': []
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
    registered = users.find_one({'username': {'$regex': username, '$options': 'i'}, 'password': password})
    if registered is not None:
        session['username'] = username
        login = True
        return redirect(url_for('all_recipes', num=1))
    login = False    
    return render_template('index.html', login=login)

""" Redirects guest users to website home page """
@app.route('/guest_user')
def guest_user():
    return redirect(url_for('all_recipes', num=1))

""" Logout a user by removing username from session """
@app.route('/login')
def logout():
    session.clear()
    return render_template('index.html')

""" My recipes page """
@app.route('/my_recipes/<username>')
def my_recipes(username):
    recipes=mongo.db.recipes.find()
    cuisines =  mongo.db.cuisines.find()
    dishes=mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    if username is not None:
        my_recipes=mongo.db.recipes.find({'recipe_author_name': {'$regex': username, '$options': 'i'}}).sort([("upvotes", -1)])
        total_my_recipes=my_recipes.count()
        print(username)
    return render_template("myrecipes.html", recipes=recipes, dishes=dishes, cuisines=cuisines, my_recipes=my_recipes, 
                            users=users, total_my_recipes=total_my_recipes, allergens=allergens)    

""" Favourite recipes page """
@app.route('/add_fav_recipes/<username>/<recipe_id>/<title>')
def add_fav_recipe(username, recipe_id, title):
    if username is not None:
        mongo.db.users.update({'username': username}, {'$push': {'fav_recipes': [recipe_id, title]}})
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, {'$push': {'fav_by_users': username}})
        return redirect(url_for('the_recipe', recipe_id=recipe_id, recipe_title= title))

@app.route('/fav_recipes/<username>')
def fav_recipes(username):
    recipes=mongo.db.recipes.find()
    cuisines =  mongo.db.cuisines.find()
    dishes=mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    this_user=mongo.db.users.find_one({'username': username})
    fav_recipe_count = len(this_user['fav_recipes']) 
    return render_template("favrecipes.html", recipes=recipes, dishes=dishes, cuisines=cuisines, fav_recipe_count = fav_recipe_count,
                            users=users, allergens=allergens, this_user=this_user)    
    

""" Home page displaying all uploaded recipes """
@app.route('/all_recipes/page:<num>')
def all_recipes(num):
    recipes=mongo.db.recipes.find().sort([("upvotes", -1)])
    cuisines =  mongo.db.cuisines.find()
    dishes=mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    total_recipes=recipes.count()
    total_pages = range(1, math.ceil(total_recipes/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = recipes.skip(skip_num).limit(8)
    if total_recipes < 8:
        page_count = total_recipes
    if (int(num) * 8) < total_recipes:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - total_recipes
        
    return render_template("home.html", recipes=recipes, num=num, dishes=dishes, cuisines=cuisines, total_pages=total_pages, skip_num=skip_num, 
                            page_count=page_count,recipes_per_page=recipes_per_page, users=users, total_recipes=total_recipes, allergens=allergens)


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
    return redirect(url_for('all_recipes', num=1))
  
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
    return redirect(url_for('all_recipes', num=1)) 

""" Displays all cuisines in MongoDB """
@app.route('/all_cuisines')
def all_cuisines():
    recipes = mongo.db.recipes.find()
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    return render_template("allcuisines.html", cuisines=cuisines, dishes=dishes,
                            recipes=recipes, users=users, allergens=allergens)

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
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    cuisine=mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template('editcuisine.html', cuisine=cuisine, dishes=dishes, users=users,
                            cuisines=cuisines, allergens=allergens)    

""" Send form data to update cuisine in MongoDB """ 
@app.route('/update_cuisine/<cuisine_id>', methods=["POST"])
def update_cuisine(cuisine_id):
    recipes = mongo.db.recipes.find()
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    new_cuisine = request.form.get('cuisine_name')
    cuisine=mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    distinct_cuisines = mongo.db.recipes.distinct('cuisine_name')
    if new_cuisine == cuisine['cuisine_name']:
        return redirect(url_for('all_cuisines'))
    elif cuisine['cuisine_name'] in distinct_cuisines:
        edit_cuisine = False
        return render_template('editcuisine.html', edit_cuisine=edit_cuisine, cuisines=cuisines, dishes=dishes, recipes=recipes,
                            users=users, allergens=allergens, cuisine=cuisine)
    else:
        cuisine.update({'_id': ObjectId(cuisine_id)}, {'cuisine_name': request.form.get('cuisine_name')})
        return redirect(url_for('all_cuisines'))  

""" Removes a cuisine from MongoDB """
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    recipes = mongo.db.recipes.find()
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    cuisine = mongo.db.cuisines
    distinct_cuisines = mongo.db.recipes.distinct('cuisine_name')
    this_cuisine =  mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)})
    if this_cuisine['cuisine_name'] in distinct_cuisines:
        delete_cuisine = False
        return render_template('allcuisines.html', delete_cuisine=delete_cuisine, cuisines=cuisines, dishes=dishes, recipes=recipes,
                            users=users, allergens=allergens)
    else: 
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
    recipes=mongo.db.recipes.find()
    dishes=mongo.db.dishes.find()
    cuisines=mongo.db.cuisines.find()
    allergens=mongo.db.allergens.find()
    users=mongo.db.users.find()
    dish = mongo.db.dishes.find_one({"_id": ObjectId(dish_id)})
    return render_template('editdish.html', dish=dish, recipes=recipes, dishes=dishes,
                            users=users, cuisines=cuisines, allergens=allergens)    

""" Send form data to update the dish in MongoDB """ 
@app.route('/update_dish/<dish_id>', methods=["POST"])
def update_dish(dish_id):
    recipes = mongo.db.recipes.find()
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    new_dish = request.form.get('dish_type')
    distinct_dishes = mongo.db.recipes.distinct('dish_type')
    dish =  mongo.db.dishes.find_one({'_id': ObjectId(dish_id)})
    if new_dish == dish['dish_type']:
        return redirect(url_for('all_dishes'))
    elif dish['dish_type'] in distinct_dishes:
        edit_dish = False
        return render_template('editdish.html', edit_dish=edit_dish, cuisines=cuisines, dishes=dishes, recipes=recipes,
                            users=users, allergens=allergens, dish=dish)
    else:
        dish.update({'_id': ObjectId(dish_id)}, {'dish_type': request.form.get('dish_type')})
        return redirect(url_for('all_dishes'))  

        

""" Remove the dish in MongoDB """ 
@app.route('/delete_dish/<dish_id>')
def delete_dish(dish_id):
    recipes = mongo.db.recipes.find()
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    dish = mongo.db.dishes
    distinct_dishes = mongo.db.recipes.distinct('dish_type')
    this_dish =  mongo.db.dishes.find_one({'_id': ObjectId(dish_id)})
    if this_dish['dish_type'] in distinct_dishes:
        delete_dish = False
        return render_template('alldishes.html', delete_dish=delete_dish, cuisines=cuisines, dishes=dishes, recipes=recipes,
                            users=users, allergens=allergens)
    else: 
        dish.remove({'_id': ObjectId(dish_id)})
        return redirect(url_for('all_dishes'))  


""" Search by Cuisine """  
@app.route('/search_cuisine/<cuisine_name>/page:<num>')
def search_cuisine(cuisine_name, num):
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    cuisine_result = recipes.find({'cuisine_name': cuisine_name}).sort([("upvotes", -1)])
    cuisine_count = cuisine_result.count()
    total_pages = range(1, math.ceil(cuisine_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = cuisine_result.skip(skip_num).limit(8)
    if cuisine_count < 8:
        page_count = cuisine_count
    elif (int(num) * 8) < cuisine_count:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - cuisine_count
    return render_template('searchcuisine.html', recipes_per_page = recipes_per_page, num=num, cuisine_name = cuisine_name,
                            skip_num=skip_num, total_pages=total_pages, page_count=page_count, count = cuisine_count, cuisines=cuisines, dishes=dishes, users=users, allergens=allergens)

""" Search by dish types """
@app.route('/search_dish/<dish_type>/page:<num>')
def search_dish(dish_type, num):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    dish_result = recipes.find({'dish_type': dish_type}).sort([("upvotes", -1)])
    dish_count = dish_result.count()
    total_pages = range(1, math.ceil(dish_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = dish_result.skip(skip_num).limit(8)
    if dish_count < 8:
        page_count = dish_count
    elif (int(num) * 8) < dish_count:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - dish_count
    return render_template('searchdish.html', dish_type=dish_type, num=num, total_pages=total_pages,page_count=page_count,
                            skip_num=skip_num, recipes_per_page=recipes_per_page, count = dish_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens) 

""" Search by authors """
@app.route('/search_author/<author_name>/page:<num>')
def search_author(author_name, num):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    author_result = recipes.find({'recipe_author_name': author_name}).sort([("upvotes", -1)])
    author_count = author_result.count()
    total_pages = range(1, math.ceil(author_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = author_result.skip(skip_num).limit(8)
    if author_count < 8:
        page_count = author_count
    elif (int(num) * 8) < author_count:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - author_count
    return render_template('searchauthor.html', total_pages = total_pages, author_name=author_name, recipes_per_page=recipes_per_page,
                            skip_num=skip_num, page_count=page_count, num=num, count = author_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)

""" Search by allergens """
@app.route('/search_allergen/<allergen_name>/page:<num>')
def search_allergen(allergen_name, num):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    allergen_result = recipes.find({'allergen_name':{'$not': {'$eq': allergen_name}}}).sort([("upvotes", -1)])
    allergen_count = allergen_result.count()
    total_pages = range(1, math.ceil(allergen_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = allergen_result.skip(skip_num).limit(8)
    if allergen_count < 8:
        page_count = allergen_count
    elif (int(num) * 8) < allergen_count:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - allergen_count
    return render_template('searchallergen.html', num = num, allergen_name=allergen_name, total_pages = total_pages, 
                            skip_num=skip_num, page_count=page_count, recipes_per_page=recipes_per_page, count = allergen_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)


""" Search by keyword """
@app.route('/search_keyword', methods=['POST'])
def insert_keyword():
    keyword = request.form.get('keyword')
    return redirect(url_for('search_keyword', num=1, keyword=keyword) ) 
    
@app.route('/search_keyword/<keyword>/page:<num>')
def search_keyword(keyword, num):
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
    keyword_result = recipes.find({"$text": {"$search": keyword}}).sort([("upvotes", -1)])
    keyword_count = keyword_result.count()
    total_pages = range(1, math.ceil(keyword_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = keyword_result.skip(skip_num).limit(8)
    if keyword_count < 8:
        page_count = keyword_count
    elif (int(num) * 8) < keyword_count:
        page_count = int(num) * 8
    else:
        page_count = int(num) * 8 - keyword_count
    return render_template('searchkeyword.html', total_pages = total_pages, num=num, keyword=keyword, recipes_per_page=recipes_per_page,
                            skip_num=skip_num, page_count=page_count, count = keyword_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)

""" Function to upvote a recipe """
@app.route('/recipe_upvotes/<recipe_id>/<author>/<title>/<username>', methods=["POST"])
def recipe_upvotes(recipe_id, title, author, username):
    recipes =  mongo.db.recipes
    users = mongo.db.users
    
    if users.find_one({'$and':[{'username': {'$regex': username, '$options': 'i'}},
    {'upvoted_recipes': (recipe_id, title)}]}) is None and author.lower() != username.lower():
        recipes.update(
            {'_id': ObjectId(recipe_id)},
            {'$inc': {"upvotes": 1}})
        users.update(
            {'username': username},
            {'$push': {'upvoted_recipes': (recipe_id, title)}})
    return redirect(url_for('all_recipes'))


        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)
    
