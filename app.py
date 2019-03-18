import os
from flask import Flask, render_template, redirect, url_for, request, session, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:mariam83@ds125945.mlab.com:25945/recipes'
app.config['SECRET_KEY'] = '[R@ndom:-B]'  
mongo = PyMongo(app)

success = Markup('<p>You are successfully registered. Please login below.</p>')
failure1 = Markup('<p>Sorry that username already exists</p>')
failure2 = Markup('<p>Login failed. Incorrect username or/and password.</p>')
Login = Markup('<i class="fas fa-sign-in-alt"></i> Login')
Logout = Markup('<i class="fas fa-sign-out-alt"></i> Logout')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    users = mongo.db.users
    registered = users.find_one({'username': username})
    if registered is None:
        users.insert_one({
            'username': username,
            'fullname': fullname,
            'password': password
        })
        return render_template('index.html', success = success)
    return render_template('index.html', failure = failure1)
        

@app.route('/logout', methods=['POST'])
def login():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    users = mongo.db.users
    registered = users.find_one({
        'username': username,
        'password': password
    })
    recipes=mongo.db.recipes.find()
    if registered is not None:
        session['username'] = username
        return render_template('home.html', user_status = Logout, recipes=recipes)
    return render_template('index.html', failure = failure2)

@app.route('/login')
def guest_user():
    recipes=mongo.db.recipes.find()
    return render_template('home.html', user_status = Login, recipes=recipes)

@app.route('/all_recipes')
def all_recipes():
    dishes=mongo.db.dishes.find()
    recipes=mongo.db.recipes.find()
    total_recipes=recipes.count()
    return render_template("home.html", recipes=recipes, dishes=dishes, total_recipes=total_recipes)
    
@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    recipes=mongo.db.recipes
    return render_template("recipe.html",
                        recipe = recipes.find_one({'_id': ObjectId(recipe_id),'recipe_title': recipe_title}))
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    cuisines=mongo.db.cuisines.find(),
    dishes=mongo.db.dishes.find(),
    allergens=mongo.db.allergens.find())

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('editrecipe.html',  
                        recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}),
                        cuisines = mongo.db.cuisines.find(),
                        dishes = mongo.db.dishes.find(),
                        allergens = mongo.db.allergens.find())

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe =  mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
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
  
   
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    doc ={}
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

    recipe = doc
    recipes=mongo.db.recipes 
    recipes.insert_one(recipe)
    return redirect(url_for('all_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe =  mongo.db.recipes
    recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes')) 

@app.route('/all_cuisines')
def all_cuisines():
    all_cuisines=mongo.db.cuisines.find()
    return render_template("allcuisines.html", cuisines=all_cuisines)


@app.route('/add_cuisine')
def add_cuisine():
    return render_template("addcuisine.html",
    cuisines=mongo.db.cuisines.find())

@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines=mongo.db.cuisines
    cuisine = request.form.to_dict()
    cuisines.insert_one(cuisine)
    return redirect(url_for('all_cuisines'))
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    cuisine=mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template('editcuisine.html',
                            cuisine=cuisine)    
 
@app.route('/update_cuisine/<cuisine_id>', methods=["POST"])
def update_cuisine(cuisine_id):
    cuisine =  mongo.db.cuisines
    cuisine.update( 
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')}
        )
    return redirect(url_for('all_cuisines'))  

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    cuisine =  mongo.db.cuisines
    cuisine.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('all_cuisines'))       
 
@app.route('/all_dishes')
def all_dishes():
    all_dishes=mongo.db.dishes.find()
    return render_template("alldishes.html", dishes=all_dishes)


@app.route('/add_dish')
def add_dish():
    return render_template("adddish.html",
    dishes=mongo.db.dishes.find())

@app.route('/insert_dish', methods=['POST'])
def insert_dish():
    dishes=mongo.db.dishes
    dish = request.form.to_dict()
    dishes.insert_one(dish)
    return redirect(url_for('all_dishes'))
    
@app.route('/edit_dish/<dish_id>')
def edit_dish(dish_id):
    dish=mongo.db.dishes.find_one({"_id": ObjectId(dish_id)})
    return render_template('editdish.html',
                            dish=dish)    
 
@app.route('/update_dish/<dish_id>', methods=["POST"])
def update_dish(dish_id):
    dish =  mongo.db.dishes
    dish.update( 
        {'_id': ObjectId(dish_id)},
        {'dish_type': request.form.get('dish_type')}
        )
    return redirect(url_for('all_dishes'))  

@app.route('/delete_dish/<dish_id>')
def delete_dish(dish_id):
    dish =  mongo.db.dishes
    dish.remove({'_id': ObjectId(dish_id)})
    return redirect(url_for('all_dishes')) 

@app.route('/search/<dish_type>')
def search(dish_type):
    dish = mongo.db.dishes
    dish.find({'dish_type':'Soup'})
    
  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)
    
