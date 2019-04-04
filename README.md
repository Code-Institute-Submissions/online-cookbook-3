# Online Cookbook
This website is my third Milestone project in Full Stack web developer course run by Code Institute. 
It is designed to serve as an online recipe book for the users where they can view, favourite and upvote other recipes. Moreover, they can
add their own recipe.

## UX
#### User Stories

###### User Story 
As a user, I can see the summary of all recipes on website.

###### User Story 
As a user, I can filter to see the desired recipe.

###### User Story 
As a registered user, I can upvote other recipes and save my favourite recipes. 

###### User Story 
As a registered user, I can add/edit my own recipe to the website. 

## Features
## Limitations
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
 


