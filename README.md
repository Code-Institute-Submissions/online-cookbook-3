# Online Cookbook
This website is my third Milestone project in Full Stack web developer course run by Code Institute. 
It is designed to serve as an online recipe book for the users where they can view, favourite and upvote other recipes. Moreover, they can
add, edit and delete their own recipes.

## Database Schema
[Mongodb](https://mlab.com/) was used to create database for the website. The database designing process was based on
two factors:
* information to display on the website
* queries required to display that information

Some queries were easy to foresee and others came into light later on during the process of development. 
As a result, the database kept evolving over time. For example, it was decided to change the look of *favourite* 
and *thumbs up* icon for the users who have already favourited or upvoted a recipe. As a result of this need, 
fields like 'fav_by_users' and 'upvoted_by_users' were added to the database.

Final database schema diagram can be found in the folder **Database Schema > dbschema-cookbook.JPG**

The final database schema consists of five collections recipes, users, allergens, cuisines and dishes. Details
of each field is given below:

###### Recipes

    Recipes collection includes following fields:
    
    * _id (ID of the recipe)
    * recipe_title (Title of recipe)
    * recipe_author_name (Username who added the recipe to the website)
    * recipe_image_url (Recipe image URL)
    * recipe_short_description (Short description of recipe)
    * recipe_prep_time (Preparation time for recipe)
    * recipe_cook_time (Cooking time for recipe)
    * total_time (Total time for recipe)
    * recipe_serves (Recipe servings)
    * allergen_name (List of all the allergens contained in the recipe)
    * cuisine_name (Cuisine name e.g. English)
    * dish_type (Type of dish e.g. Starter)
    * recipe_ingredients (List of all ingredients with their measurements required for recipe)
    * recipe_steps (List of all steps for making the recipe)
    * upvotes (Number of upvotes for recipes)
    * upvoted_by_users (List of usernames who upvoted the recipe)
    * fav_by_users (List of usernames who favourited the recipe)

###### Users

    Users collection includes following fields:
    
    * _id (ID of the user)
    * fullname (Full name of registered user)
    * username (Username of registered user)
    * password (Password of registered user)
    * upvoted_recipes (List of recipe id's and title upvoted by user)
    * fav_recipes (List of recipe id's and title favourited by user)
  
###### Dishes

    Dishes collection includes following fields:
    
    * _id (ID of the dish type)
    * dish_type (Type of dish e.g. Starter)
    
###### Cuisines

    Cuisines collection includes following fields:
    
    * _id (ID of the cuisine name)
    * cuisine_name (Cuisine name e.g. English)

###### Allergens

    Allergens collection includes following fields:
    
    * _id (ID of the allergen name)
    * allergen_name (Allergen name e.g. Peanuts)


## UX
Wireframes were created using *Pencil* software. 

Wireframes can be found in the folder **Wireframes > cookbook-wireframe.pdf**.
The wireframe only served as a starting point in building the website as the final website design 
is quite different to the design in wireframe. 

[Materializecss](http://archives.materializecss.com/0.100.2/) framework version 0.100.2 was used to design the website. 

###### Register/Login Page
The [tabs](http://archives.materializecss.com/0.100.2/tabs.html) structure of materializecss was used to design sign in
and sign up forms. Placeholders are used for each input field.

For good user experience, users are not forced to register to visit the website. They can explore the website as a guest user. 
As a guest user, they have access to view recipes but do not have the privilege to upvote a recipe or add their own recipe until 
they become a registered user.

###### Navigation

Materializecss [Navbar](http://archives.materializecss.com/0.100.2/navbar.html#right) is used for navigation.
For good user experience:
* [Mobile Collapse Button](http://archives.materializecss.com/0.100.2/navbar.html#mobile-collapse) for mobile view
* [Dropdown Menu](http://archives.materializecss.com/0.100.2/navbar.html#navbar-dropdown) used for categories for filtering all recipes based on that category
* [Search bar](http://archives.materializecss.com/0.100.2/navbar.html#search-docs) used for search by keywords
* *Welcome, username* is displayedfor registered users.
* On clicking, *Welcome, username* registered user has option to go to *My recipes*, *Favourite recipes* and *Logout*
* Sign in and Sign up is displayed for guest users.
* Clicking, on *sign in* takes the user to login page with *sign in* tab active.
* Clicking on *sign up* takes the user to login page with *sign up* tab active

###### Home Page
Home page displays all available recipes on the website.
For good user experience following features are added:
* [pagination](http://archives.materializecss.com/0.100.2/pagination.html) is used
* maximum 8 recipes are displayed per page
* range of recipes displayed from the total number is shown on each page
* Materializecss [card](http://archives.materializecss.com/0.100.2/cards.html#reveal) are used to display recipes
* All recipes are sorted according to number of upvotes in descending order
* Favourite and upvote icon displayed to save the recipe as favourite recipe or upvote a recipe (for registered users only)
* Clicking on *View the recipe* takes the user to page with detailed view of recipe.
* Page is made responsive by allowing four recipes per row on desktop view, two per row on tablets and one per row on mobile.

###### Add a Recipe
For good user experience, following features are added:
* Easy to follow format of form
* Placeholders are used to indicate what information should be entered in the input field
* Indicated that all fields are required

###### Edit a Recipe
For good user experience, following features are added:
* features in *Add a recipe* applies here as well
* input fields are populated to display user existing information of recipe

###### Manage Categories
For good user experience, following features are added:
* Display number of recipes in a category
* Add/Edit/delete new category
* Disallow user to add/edit/delete a recipe if it is not empty

###### Recipe Page
For good user experience, following features are added:
* Allow user to edit, delete, upvote and favourite a recipe
* Display important recipe information e.g. ingredients, method, cook time, number of upvotes etc
* Display to the user if they have already upvoted the recipe
* Display to the user is they have already favourited the recipe
* Allow user to remove the recipe from favourites by clicking icon again
* Tooltip is used to display the icon function and status.

#### User Stories

###### User Story 1
I can visit the website as a guest user.

###### User Story 2
I can sign up and then sign in as a registered user.

###### User Story 3
I get an error message explaining me why I am unable to sign in or sign up.

###### User Story 4
I am able to log out.

###### User Story 5
I am able to add, edit or delete a recipe.

###### User Story 6
I am unable to edit or delete other user's recipes.

###### User Story 7
I am able to upvote other users recipes but not my own recipes.

###### User Story 8
I am unable to upvote a recipe more than once.

###### User Story 9
I am able to add and remove recipe from my favourite recipes.

###### User Story 10
I am able to see all recipes added by me.

###### User Story 11
I am able to see all recipes on the website.

###### User Story 12
I am able to see details of a recipe.

###### User Story 13
I am able to filter through the recipes based on some category.

###### User Story 14
I am able to filter through the recipes based on some keywords.

###### User Story 15
I am able to see the total number of recipes in a category.

###### User Story 16
I am able to add new dish type or cuisine name.

###### User Story 17
I am unable to delete or edit a non-empty dish type or cuisine name.

###### User Story 18
I am able to use the website on my mobile or tablet.


## Features
Following features are used to satisfy the needs of all users:
* User 1 can visit the website as a guest user by just clicking CONTINUE button on login page.
* User 2 can use Sign Up form to register and then Sign In form to sign in as a regsitered user.
* User 3 can see the error message displayed in following scenarios:
  * SIGN UP - entering existing username will throw an error message
  * SIGN IN - entering incorrect username or/and password will throw an error message
* User 4 can log out by clicking *Welcome, username* and choosing option *logout*.
* User 5 can click on *Add a recipe* and fill in the form to add recipe. To edit or delete a recipe, user 5
  can click on *View the recipe* on added recipe card. Then on recipe page, they can click edit or delete button
  to edit or delete recipe.
* No user is allowed to edit or delete someone else's recipe, which satisfy needs of User 6.
* All users can upvote each others recipes but not their own, which satisfy needs of User 7.
* All users can upvote a recipe once only, which satisfy needs of User 8.
* All users can add or remove a recipe from their favourite recipes by clicking the *favourite* icon, which satisfy needs of User 9.
* All users can go to *My recipes* and see the list of all recipes uploaded by them. This satisfy needs of User 10.
* All users can go to home page by clicking on *Home* or *My Cookbook* and see the list of all recipes. This satisfy needs of User 11.
* All users can click on *View the recipe* on recipe card and go to the page with recipe details. This satisfy needs of User 12.
* All users can filter through the recipes by clicking on *Dish Types*, *Cuisines*, *Author* or *Allergens* and then selecting the category
  that they want to base their search on. This satisfy needs of User 13.
* All users can enter keyword(s) in search bar in the navigation to filter recipes by keywords. This satisfy needs of User 14.
* All pages with recipe display shows the users total number of recipes, range of recipes displayed and page number (if more than one). 
  This satisfy needs of User 15.
* All users can add a new dish type or cuisine name. This satisfy needs of User 16.
* All users can edit or delete an empty dish type or cuisine name. This satisfy needs of User 17.
* Website is responsive so all users can use it on mobile and tablets. This satisfy needs of User 18.

## Limitations
Following features are highly desirable and should be added to the website:
* Date recipe added so the recipe cards can display *Added today*, *Added less than a month ago* etc
* Instead of upvotes *Five star rating* with detailed reviews.
* *Add a recipe* form can be improved to upload a picture from computer.
* Pictures added to website are made same size.
* *Add a recipe* form can be improved by adding measurement units field separately.


## Technologies Used

The website is designed using following technologies:
- HTML
- CSS
- JavaScript
- Jquery
- Font Awesome library
- Materialize
- Pencil

## Testing
All tests were carried out manually. Testing process was as follows:
##### Login Page
###### Logo
* Click on *logo* and verify that page refreshes.

###### Guest User
* Click on *continue*  button and verify that website home page appears.

###### Sign In
* Click on *sign in* button with all or some incomplete fields and verify that 
  an error message (next to the first incomplete field) appears stating, 'Please 
  fill in this field'. Form does not get submitted unless all input fields are filled.
* Enter incorrect username or/and password, click on *sign in* button and verify 
  that error message appears stating, 'Login failed. Incorrect username or/and 
  password. Please try again.'
* Enter correct username (case-insensitive) and password (case-sensitive), click
  on *sign in* button and verify that website home page appears

###### Sign Up
* Click on *sign up* button with all or some incomplete fields and verify that 
  an error message (next to the first incomplete field) appears stating, 'Please 
  fill in this field'. Form does not get submitted unless all input fields are filled.
* Enter existing username (case-insensitive), any full name and password, click 
  on *sign up* button and verify that error message appears stating, 'Sorry that
  username already exists. Please use a different username.'
* Enter new username, any full name and password, click on *sign up* button and 
  verify that error message appears stating, 'You are successfully registered. 
  Please login below.'

##### Home Page
###### Navigation links
* Click on *logo* or *Home* and verify that home page appears.
* Click on *Add Recipe* and verify that page appears with *Add a Recipe* form. (Registered users only)
* Click on *Manage categories* and verify that dropdown menu appears with menu 
  items *All cuisines* and *All dish types*. (Registered user only)
* Click on *All cuisines* and verify that page appears with the list of all 
  available cuisines created by users. (Registered user only)
* Click on *All dish types* and verify that page appears with the list of all 
  available dish types created by users.(Registered user only)
* Click on *Welcome, username* and verify that dropdown menu appears with menu
  items *My recipes*, *Favourite recipes* and *Logout*.(Registered user only)
* Click on *My recipes* and verify that all recipes added by current user appears
  on *My recipes* webpage. (Registered users only)
* Click on *Favourite recipes* and verify that all recipes saved as favourite by
  user appears on *Favourite recipes* webpage. (Registered user only)
* Click on *Logout* and verify that session ends and login page appears.(Registered user only)
* Click on *Login* and verify that login page appears.(Guest user only)
* Click on *Dish Types*, *Cuisines*, *Authors* or *Allergens* and verify that 
  dropdown menu shows all available dish types, cuisine names, author names and 
  14 main allergens respectively.

###### All Recipes
* Verify that page loads with a display of all recipes available on the website.
* Verify that all recipes are sorted in the descending order of upvotes.

###### Filtered Recipes
* Click on any XYZ dish type in *Dish Types* and verify that only recipes with 
  dish type XYZ will appear. 
* Click on any XYZ cuisine name in *Cuisines* and verify that only recipes with 
  cuisine name XYZ will appear.
* Click on any XYZ author name in *Authors* and verify that only recipes with 
  author name XYZ will appear.
* Click on any XYZ allergen in *Allergens* and verify that only XYZ allergen 
  free recipes will appear.
* Enter word(s) in *Search* field and verify that the recipes that contain these
  words in title, ingredients, cuisine name, dish type or author name will appear.
* Verify that all search results are sorted in the descending order of upvotes.

###### Pagination
* Go to home page and verify that maximum 8 recipes are displayed per page.
* Carry out any search (using dropdown menu or search field) and verify that 
  maximum 8 recipes are displayed per page for all searches.
* As a result of search or otherwise, verify that the page always display correct 
  total on the leftmost side of pagination.
* As a result of search or otherwise, verify that the page always display correct 
  recipes range on the leftmost side of pagination.
* Verify that previous and next arrow of pagination only appears when page number
  is greater than one.
* Click on previous or next arrow and verify that page display recipes in the 
  previous and next page respectively.
* Click on previous arrow when first page is active and verify that it is disabled.
* Click on next arrow when last page is active and verify that it is disabled.
* Click on any page number and verify that page displays the recipes on that page.
* Click on any page number and verify that active page is shown by pink background.

###### Recipe cards
* Verify that all images are responsive.
* Click on *three vertical dots* and verify that *short recipe description* slides
  up.
* Click on *thumbs up* icon and verify that upvotes number is increased only when user:
    * is registered,
    * is not the author of the recipe, and
    * has not already upvoted.
* Hover on *heart* icon and verify that tooltip appears stating 'Add to favourites'
  if the recipe is not already in *My favourite recipes*. (Registered user only)
* Hover on *heart* icon and verify that tooltip appears stating 'Added to favourites'
  if the recipe is already in *My favourite recipes*. (Registered user only)
* Click on *heart icon* and verify that if the recipe is not in *My favourite recipes*,
  then it is added and vice versa. 
* Verify that *heart icon* status is *save* if recipe is not in *My favourite recipes*.
* Verify that *heart icon* status changes to *saved* if recipe is in *My favourite recipes*.
* Click on *View this Recipe* and verify that webpage with all recipe details appear.


##### Add Recipe Page (Registered users only)
* Click on **Save recipe** button with all or some incomplete fields and verify that 
  an error message (next to the first incomplete field) appears stating, 'Please 
  fill in this field'. Form does not get submitted unless all input fields are filled.
* Click on *add* icon and verify that an input field for ingredient or method step
  appears with *delete* icon. 
* Click on *delete* icon and verify that the input field next to it is removed.
* Verify that at least one ingredient or method step is required to submit the form.
* Enter image in a format other than url and verify that the form is not submitted
  unless correct url format is entered.
* Click on **Save recipe** button and verify that user is redirected to home page.

##### Manage Categories (Registered users only)
###### All Cuisines/ All Dish Types 
* Click on *Edit* icon and verify that the respective edit page (*Edit Cuisine* or 
  *Edit Dish Type* ) form appears with the saved value in the input field.
* Try editing the saved cuisine name or dish type that has at least one recipe 
  linked to it, click *save changes* and verify that *error* message will appear 
  stating 'Oops, there is an error! Sorry this category name cannot be edited. A 
  category name can only be edited if it contains no recipe.'
* Try editing the Cuisine with no recipe linked to it, click *save changes* and 
  verify that it is successfully edited.
* Click *Delete* icon and verify that if at least one recipe is linked to it, 
  an *error* message will appear stating 'Oops, there is an error! Sorry this 
  category name cannot be deleted. A category name can only be deleted if it 
  contains no recipe.'
* Click *Delete* icon and verify that if at no recipe is linked to it and verify 
  that it is successfully deleted.

##### Recipe Details Page 
* Click on 'View this Recipe' button on any recipe card (either on home page or 
  any other webpage with recipe cards) and verify that *Edit* and *Delete* icon 
  only appears if user is the author of recipe. 
* Click on *Edit* icon and verify that *Edit recipe* form page appears. Verify 
  that all input fields are filled with the previously saved values.
* Click on *Save changes* and verify that (if all tests detailed above in 
  **Add Recipe Page** are satisfied) then recipe is successfully changed and user
  is redirected to *My Recipes* page.
* Click on *Delete* icon and verify that recipe is deleted and user is redirected to
  *My Recipes* page.

##### Dev Tools
##### HTML and CSS validator
##### Cross Browser Testing
###### Accessibility / Screen Reader Application Testing
## Deployment
## Credits
#### Content


#### Acknowledgements
 


