# Online Cookbook
This website is my third Milestone project in Full Stack web developer course run by [Code Institute](https://codeinstitute.net/). 

It is designed to serve as an online recipe book for the users where they can view, favourite and upvote recipes. Moreover, they can
add, edit and delete their own recipes.

## Database Schema
[Mongodb](https://mlab.com/) was used to create database for the website. The database designing process was based on
two factors:
* information to display on the website
* queries required to display that information

Some queries were easy to foresee and others came into light during the development process. 
As a result, the database kept evolving over time. 

For example, it was decided to change the look of *favourite* 
and *thumbs up* icon for the users who have already favourited or upvoted a recipe. As a result of this need, 
fields like 'fav_by_users' and 'upvoted_by_users' were added to the database.

Final database schema diagram can be found in the folder **Database Schema > dbschema-cookbook.JPG**

The final database schema consists of five collections recipes, users, allergens, cuisines and dishes. Details
of each field is given below:

##### Recipes

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
    * recipe_ingredients (List of all ingredients with their measurements required for the recipe)
    * recipe_steps (List of all steps for making the recipe)
    * upvotes (Number of upvotes for the recipe)
    * upvoted_by_users (List of usernames who upvoted the recipe)
    * fav_by_users (List of usernames who favourited the recipe)

##### Users

    Users collection includes following fields:
    
    * _id (ID of the user)
    * fullname (Full name of registered user)
    * username (Username of registered user)
    * password (Password of registered user)
    * upvoted_recipes (List of recipe id's and title upvoted by user)
    * fav_recipes (List of recipe id's and title favourited by user)
  
##### Dishes

    Dishes collection includes following fields:
    
    * _id (ID of the dish type)
    * dish_type (Type of dish e.g. Starter)
    
##### Cuisines

    Cuisines collection includes following fields:
    
    * _id (ID of the cuisine name)
    * cuisine_name (Cuisine name e.g. English)

##### Allergens

    Allergens collection includes following fields:
    
    * _id (ID of the allergen name)
    * allergen_name (Allergen name e.g. Peanuts)


## UX
Wireframes were created using *Pencil* software. 

Wireframes can be found in the folder **Wireframes > cookbook-wireframe.pdf**.
The wireframe only served as a starting point in building the website as the final website design 
is quite different to the design in wireframe. 

[Materializecss](http://archives.materializecss.com/0.100.2/) framework version 0.100.2 was used to design the website. 

[Font awesome icons](https://fontawesome.com/icons) was used for some icons that were not available in materializecss icons.

##### Register/Login Page
Materailizecss [tabs](http://archives.materializecss.com/0.100.2/tabs.html) structure was used for sign in and sign up forms. 

For good user experience, following features were taken into consideration:
* placeholders are used for each input field
* users are not forced to register and can explore the website as a guest user
* only registered users have the privilege to upvote a recipe or add their own recipe 

##### Navigation
Materializecss [Navbar](http://archives.materializecss.com/0.100.2/navbar.html#right) is used for navigation.

For good user experience, following features were taken into consideration:
* [mobile Collapse Button](http://archives.materializecss.com/0.100.2/navbar.html#mobile-collapse) is used for mobile view
* [dropdown Menu](http://archives.materializecss.com/0.100.2/navbar.html#navbar-dropdown) is used for dish types, cuisines, author and allergens in navigation bar, for filtering recipes based on that category.
* [search bar](http://archives.materializecss.com/0.100.2/navbar.html#search-docs) is added for filtering recipes using keyword(s)
* 'welcome, *username*' is displayed for registered users.
* on clicking 'Welcome, *username*', registered users has the option to go to *My recipes*, *Favourite recipes* or *Logout*
* sign in and sign up is displayed for guest users.
* clicking, on *sign in* takes the guest user to login page with *sign in* tab active.
* clicking on *sign up* takes the guest user to login page with *sign up* tab active

##### Home Page
Home page displays all available recipes on the website.

For good user experience, following features were taken into consideration:
* [pagination](http://archives.materializecss.com/0.100.2/pagination.html) is used
* maximum of 8 recipes are displayed per page
* total number of recipes is displayed
* range of recipes on the page is displayed
* materializecss [card](http://archives.materializecss.com/0.100.2/cards.html#reveal) are used for each recipe display
* favourite and upvote icons displayed
* recipes are sorted in descending order of upvotes
* page is made responsive by showing four recipes per row on desktop view, two per row on tablets and one per row on mobile.

##### Add a Recipe
For good user experience, following features were taken into consideration:
* easy to follow form format
* placeholders are used for each input field
* informed user that all fields are required
* dynamically add or remove input field for ingredients and steps

##### Edit a Recipe
For good user experience, following features were taken into consideration:
* features in 'Add a recipe' applies here as well
* prepopulated input and select fields with existing information about recipe

##### Manage Categories
For good user experience, following features were taken into consideration:
* display number of recipes in each category
* add a new category
* edit or delete an empty category only
* page is made responsive by showing three categories per row on desktop view, two per row on tablets 
  and one per row on mobile.

##### Recipe Page
For good user experience, following features were taken into consideration:
* display important recipe information e.g. ingredients, method, cook time, number of upvotes etc
* allow user to upvote and favourite a recipe
* allow user to edit or delete their own recipe
* display to the user if they have already upvoted the recipe
* display to the user if they have already favourited the recipe
* allow user to remove the recipe from favourites by clicking icon again
* tooltip is used to display the icon function and status.

##### My Recipes
For good user experience, following features were taken into consideration:
* allow user to see all recipes added by them
* for design consistency, materializecss [card](http://archives.materializecss.com/0.100.2/cards.html#reveal) are used for each recipe display

##### Favourite recipes
For good user experience, following features were taken into consideration:
* allow user to see their favourite recipes in one place
* for design consistency, materializecss [card](http://archives.materializecss.com/0.100.2/cards.html#reveal) are used for each recipe display

## User Stories

##### User Story 1
I can visit the website as a guest user.

##### User Story 2
I can sign up and then sign in as a registered user.

##### User Story 3
I get an error message explaining me why I am unable to sign in or sign up.

##### User Story 4
I am able to log out.

##### User Story 5
I am able to add, edit or delete a recipe.

##### User Story 6
Only I can edit or delete my recipes.

##### User Story 7
I am able to upvote other users recipes but not my own recipes.

##### User Story 8
I am unable to upvote a recipe more than once.

##### User Story 9
I am able to add and remove recipe from my favourite recipes.

##### User Story 10
I am able to see all recipes added by me.

##### User Story 11
I am able to see all recipes available on the website.

##### User Story 12
I am able to see details of a recipe.

##### User Story 13
I am able to filter through the recipes based on some category.

##### User Story 14
I am able to filter through the recipes based on some keywords.

##### User Story 15
I am able to see the total number of recipes in a category.

##### User Story 16
I am able to add new dish type or cuisine name.

##### User Story 17
I am unable to delete or edit a non-empty dish type or cuisine name.

##### User Story 18
I am able to use the website on my mobile or tablet.


## Features
Following features are used to satisfy the needs of all users:

    1.  Website can be visited as a guest user by just clicking CONTINUE button on login page.
        This satisfy the needs of user 1.
    2.  Sign In and Sign Up forms are available on login page. This satisfy the needs of user 2.
    3.  An error message is displayed in the following scenarios:
        1.  Sign Up Form - entering existing username will throw an error message
        2.  Sign In Form - entering incorrect username or/and password will throw an error message
        This satisfy the needs of user 3.
    4.  By clicking 'Welcome, username', users can choose option 'logout' to log out of website.
        This satisfy the needs of user 4.
    5.  By clicking 'Add a recipe' and then filling in the form, registered users can add a recipe. 
        To edit or delete recipe, users can click edit or delete button on the recipe view page.
        This satisfy the needs of user 5.
    6.  No user is allowed to edit or delete someone else's recipe. This satisfy the needs of user 6.
    7.  Registered users can upvote each others recipes but not their own. This satisfy the needs of 
        user 7.
    8.  Registered users can upvote a recipe only once. This satisfy the needs of user 8. 
    9.  Registered users can add or remove a recipe from their favourite recipes by clicking the 
        'favourite' icon. This satisfy the needs of user 9.
    10. Registered users can go to 'My recipes' and see the list of all recipes uploaded by them. This 
        satisfy the needs of user 10.
    11. Users can go to the home page by clicking on 'Home' or 'My Cookbook' and see the list of all 
        recipes. This satisfy the needs of user 11.
    12. Users can click on 'View the recipe' on recipe card and go to the page with recipe details. 
        This satisfy the needs of user 12.
    13. Users can filter through the recipes by clicking on 'Dish Types', 'Cuisines', 'Author' or 
        'Allergens' and then selecting the category that they want to base their search on. This satisfy 
         the needs of user 13.
    14. Users can enter keyword(s) in search bar in the navigation to filter recipes by keywords. 
        This satisfy the needs of user 14.
    15. All pages with recipe display shows the users total number of recipes, range of recipes 
        displayed and page number (if more than one). This satisfy the needs of user 15.
    16. Registered users can add a new dish type or cuisine name. This satisfy the needs of user 16.
    17. Regsitered users are not allowed to edit or delete a non-empty dish type or cuisine name. 
        This satisfy the needs of user 17.
    18. Website is responsive so all users can use it on mobile and tablets. This satisfy the needs of 
        user 18.

## Limitations
Following features are highly desirable and should be added to the website:
* Date recipe added so the recipe cards can display *Added today*, *Added less than a month ago* etc
* Instead of upvotes *Five star rating* with detailed reviews.
* *Add a recipe* form can be improved to upload a picture from computer.
* Pictures added to website are made same size.
* More than one picture is allowed to be added.
* *Add a recipe* form can be improved by adding measurement units field separately.


## Technologies Used

The website is designed using following technologies:
- HTML
- CSS
- JavaScript
- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Mongodb](https://mlab.com)
- [Jquery](https://jquery.com/download/)
- [Font Awesome library](https://fontawesome.com/icons)
- [Pencil](https://pencil.evolus.vn/)
- [Materializecss 0.100.2](http://archives.materializecss.com/0.100.2/)  


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
* Click on *Sign in* and verify that login page appears with sign in tab active.
* Click on *Sign up* and verify that login page appears with sign up tab active.
* Click on *Dish Types*, *Cuisines*, *Authors* or *Allergens* and verify that 
  dropdown menu shows all available dish types, cuisine names, author names and 
  14 main allergens respectively.

###### All Recipes
* Verify that home page loads with a display of all recipes available on the website.
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

###### Pagination/Search result summary
* Go to home page and verify that maximum 8 recipes are displayed per page.
* Carry out any search (using dropdown menu or search field) and verify that 
  maximum 8 recipes are displayed per page for all searches.
* As a result of search or otherwise, verify that the page always display correct 
  total on the leftmost side of pagination.
* As a result of search or otherwise, verify that the page always display correct 
  recipes range on the leftmost side of pagination.
* Verify that pagination only appears when page number is greater than one.
* Click on previous or next arrow and verify that page display recipes in the 
  previous and next page respectively.
* Click on previous arrow when first page is active and verify that it is disabled.
* Click on next arrow when last page is active and verify that it is disabled.
* Click on any page number and verify that page displays the recipes on that page.
* Click on any page number and verify that active page is shown by pink background.

###### Recipe cards
* Verify that all images are responsive
* Verify that for guest users only *upvote* icons are displayed on recipe cards
* Verify that for registered users both *upvote* and *favourite* icons are displayed on recipe card
* Hover on *thumbs up* icon and verify that tooltip appears stating 'Upvote this recipe'
  if the recipe is not already upvoted. (Registered user only)
* Hover on *thumbs up* icon and verify that tooltip appears stating 'Already upvoted'
  if the recipe is already upvoted. (Registered user only)
* Hover on *favourite* icon and verify that tooltip appears stating 'Add to favourites'
  if the recipe is not already in *My favourite recipes*. (Registered user only)
* Hover on *favourite* icon and verify that tooltip appears stating 'Remove from favourites'
  if the recipe is already in *My favourite recipes*. (Registered user only)
* Verify that *favourite* icon label is *Add* if recipe is not in *My favourite recipes*.
* Verify that *favourite* icon label changes to *Remove* if recipe is in *My favourite recipes*.
* Click on *favourite* icon and verify that if the recipe is not in *My favourite recipes*,
  then it is added and vice versa. 
* Click on *View this Recipe* and verify that webpage with all recipe details appear.
* Click on *three vertical dots* and verify that *short recipe description* slides  up.
* Click on *thumbs up* icon and verify that upvotes number is increased only when user:
    * is registered,
    * is not the author of the recipe, and
    * has not already upvoted.


##### Add Recipe Page (Registered users only)
* Click on 'Save recipe' button with all or some incomplete fields and verify that 
  an error message (next to the first incomplete field) appears stating, 'Please 
  fill in this field'. Form does not get submitted unless all input fields are filled.
* Click on *add* icon and verify that an input field for ingredient or method step
  appears with *delete* icon. 
* Click on *delete* icon and verify that the input field next to it is removed.
* Verify that at least one ingredient or method step is required to submit the form.
* Enter image in a format other than url and verify that the form is not submitted
  unless correct url format is entered.
* When all the fields are filled in, click on 'Save recipe' button and verify that 
  * user is redirected to *My recipes* page and
  * new recipe is added to the page

##### Recipe Details Page 
* Click on 'View this Recipe' button on any recipe card (either on home page or 
  any other webpage with recipe cards) and verify that recipe page opens with recipe details
  in it.
* Verify that *Edit* and *Delete* icon only appears if user is the author of recipe. 
* Verify that *Favourite* icon only appears if the user is registered.
* Click on *Edit* icon and verify that *Edit recipe* form page appears. 
  * Verify that all input fields are prepopulated with the previously saved values.
  * Verify that all the tests mentioned in *Add Recipe Page* section pass here too.
  * Click on *Save changes* and verify that 
    * user is redirected to *My Recipes* page
    * recipe is successfully changed
* Click on *Delete* icon and verify that 
    * user is redirected to *My Recipes* page
    * recipe is deleted from *My recipes* page and from the website
* Verify that *favourite* and *upvote* icon pass the tests mentioned in *Recipe cards* section

##### Manage Categories (Registered users only)
###### All Cuisines/ All Dish Types 
* Verify that all cuisines (or dish types) are listed with total number of recipes for that
  category in bracket (e.g. Soup(4) means 'Dish type soup have four recipes')
* Verify that *Edit* and *Delete* icons only appear next to an empty category.
* Click on *Edit* icon and verify that the respective edit page (*Edit Cuisine* or 
  *Edit Dish Type* ) form appears with the saved value in the input field.
* Edit the cuisine name (or dish type), click *save changes* and verify that user is redirected to 
  all cuisines (or all dishes) page with changes saved.
* Click on *Delete* icon and verify that cuisine name or dish type is successfully deleted.
* Click on *Add Cuisine* (or *Add Dish*) and verify that user is redirected to *Add Cuisine* (or 
  *Add dish type*) page.
* Try adding an existing cuisine name (or dish type) in the input field for *New Cuisine* (or *New dish type*), click
  *Save cuisine* (or *Save dish type*) and verify that error message is displayed 'Oops, there is an error! 
  Sorry this category name already exists. Please try a new category name.' 
* Try adding a new cuisine name (or dish type), click *Save cuisine* (or *Save dish type*) and verify that user
  is redirected to all cuisines (or all dish types) page where the new cuisine (or new dish type) is displayed.

##### Welcome, username (Registered users only)
###### My recipes 
* Verify that all recipes displayed on *My recipes* page are current users recipes.

###### Favourite recipes 
* Verify that all recipes displayed on *Favourite recipes* page are the ones favourited by 
  the current user.

###### Logout 
* Click *Logout* and verify that current user session is cleared and user is redirected to login page.

##### Responsiveness Testing:
Dev Tools, iphone X and iPad were used to test the appearance of website on mobile/tablet screen size.  
Following features were verified:
* A *Menu* icon appears on the left corner and all menu items disappear.
* On clicking *Menu* icon, side navigation slides in with all menu items.
* In login page, container widths change responsively for different screen sizes.
* Materializecss cards for displaying recipes, cuisine names and dish types rearranges responsively for different screen sizes.
* Images changes responsively for different screen sizes.
* Recipe page rearranges images and texts responsively for different screen sizes.

##### HTML and CSS validator
[W3 Validator](https://validator.w3.org/) and [CSS validators](https://jigsaw.w3.org/css-validator/) were used to validate the code. 
- HTML validator raised no issue or warnings.
- CSS validator raised warnings for 'unknown vendor extension' in CSS stylesheet. 
  Prefixes are required for box-shadow to work in old browsers. Hence these warnings are ignored!

##### Cross Browser Testing
- [CanIuse.com](https://caniuse.com/)
    - CanIuse.com website was used to check browser support for CSS codes and use correct prefixes, where required.

- The website was tested to function as expected on following browsers:
  - Chrome
  - Firefox
  - IE 
  - Edge 
  - Safari
  - Samsung A3 internet browser

###### Accessibility / Screen Reader Application Testing
Wherever possible following things were taken into consideration to make website as accessible as possible:
* aria-hidden = "true" used for icons
* label used for form fields
* alt attribute used in all images
* aria-label was used for button icons

## Deployment
##### Content
- All recipes used in this site are obtained from [allrecipes](http://allrecipes.co.uk/).

##### Media
- All recipe images used in this site are obtained from [allrecipes](http://allrecipes.co.uk/).

##### Code by others
- Bug found in materializecss **disabled** class. The class was used to disable left and right chevron in pagination but 
  only changed colour to grey and was still clickable. Code found [here](https://github.com/Dogfalo/materialize/issues/3835)  
  solved the issue by setting pointer-events to none.
- Styling headings with lines before and after were taken from [stackoverflow](https://stackoverflow.com/questions/38212963/how-to-display-a-horizontal-line-before-and-after-a-heading-in-css)
- [Flask docs](http://flask.pocoo.org/docs/1.0/quickstart/#sessions) was used to create login page backend code.
- 'Add a recipe' form required dynamically adding and removing form input fields which was taken from [Youtube video](https://www.youtube.com/watch?v=jSSRMC0F6u8)
- These three sources [flask](http://flask.pocoo.org/snippets/44/), [codementor](https://www.codementor.io/arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr) and 
  [stackoverflow](https://stackoverflow.com/questions/8676455/flask-current-page-in-request-variable) greatly helped my understanding in creating pagination.
- When my for loops didn't work in jinja template, I found solution on [stackoverflow](https://stackoverflow.com/questions/34877236/for-loop-not-working-in-jinja-flask)
- How to convert strings to integers when passed into jinja template? I found solution on [stackoverflow](https://stackoverflow.com/questions/38857366/integer-gets-converted-to-string-when-passed-into-jinja-template)
- I wanted to redirect users back to same page after clicking upvote or favourite button icon. I found solution on [stackoverflow](https://stackoverflow.com/questions/14277067/redirect-back-in-flask?noredirect=1&lq=1)

#### Acknowledgements
- I would like to thank my tutor Antonija Simic for all her help and support during the development of this project.   
- I would also like to thank other code institute students for sharing their projects which was extremely useful in designing this website. 





