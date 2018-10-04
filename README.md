Recipe Database

The purpose of this application is to achieve a database which provides the method on how to cook all recipes across many different cusines in one place, to evantually to have a database which is like wikipedia but for recipes. To allow the user to filter the results across many different option but this is more of a long term goal the same goes for to add key work filter search function. The user current has the ability to pick a username to enter the page then redirected to all the recipes. From here they can use all CRUB operation, so the can read the different recipes on my main page, create new one from the add recipe page, update or edit recipes via the edit button on the main page and finally delete the recipe from the main page. I have also included a log out function for the user.

UX:

The website is for users who want to cook dishes from different cusines and they don't know how they can start. This is where my website comes into play it will provide insigh on different cusines because they can filter search all the different cusines to pin point a cusine they may want to focus on.

The page also offers the opportunitity for users to add their own created recipe for others to use, share and enjoy which is a big aspect of this website but also for people to take a already posted recipe and to add to it, so they can put their twist on it, so if a user edits a recipe then submits it the original stays there and a new one gets added.

I feel like i have made it very easy aswell for users to edit, add and delete recipes which is very key as its the main focus of the application.

Mockups:
    mockups are found in a serperate folder on github and the folder is called mockups. mocks up were adpated on

Features:
    1. username sign up
    2. nav bar to access recipes, add recipes and log out
    3. read recipes details through header
    4. read recipes ingredients and instruction via dropdown
    5. edit recipes via edit button and function
    6. delete recipes via delete button and function
    7. add new recipes via add recipes form
    8. filter through recipes via cusine filter
    
Features to add:
These are more long term goals
    1. more filters
    2. advance registraion page
    3. username of user gets added to recipe they added
    
Technologies Used:

    1. Materialize
        To use grid layout but also so have good looking elements such as forms and nav bar, also to use icons for certain elements
        
    2. HTML and CSS
        To structure and style, the web app content, including creating the POST method form
        
    3. Flask
        For binding functions to URLs using routing
        To render HTML templates, including the use of a base template. These templates are in the templates directory
        To trigger functions on GET or POST requests
        Used for debugging
        
    4. mLab/mongodb
        To create a database for the app and to access the data in the database
        
    5. Heroku
        To deploy final version for viewing
        Project link:
        https://recipe-database.herokuapp.com/
        
    6. Git Hub
        For version control
        
Testing
    1.	Links
    
        All nav bar links work 
        All button links work such as submit button for username and the add/edit/delete recipe buttons, they redirect to the correct pages or perform the correct function
        
    2.	Text and colours
    
        They are appropriately sized and colour scheme is simple and readable
        
    3.  Post and Get functions
        
        The forms to add/edit recipes , all perform the correct action they were made to do
        when editing a recipe the previous data is already filled in
        
    4. layout
    
        layout is repsonsive across all elements thanks to materialize
        
    5. Filter cusine function
    
        when the user selects the correct option the correct recipes displays
        
    6.	Mobile and browser testing
        I tested the application on the smaller screen devices and tablets, the application performs the same but layout may be different due to smaller screen and i achieved this by the responsive design of materialize. i also performed all the test i stated above on mobile and tablet and i got the same results
        
        Application works on all latest and main browsers 

Deployment

Run Locally
    1.	Clone or download this GitHub repository using the ‘Clone or Download’ button found on the main page
    
    2.	Open the project directory using an integrated development environment (IDE) software application, such as Cloud 9
    
    3.	The project uses python 3 but Cloud 9 comes with python 3 already installed however when running the app.py file make sure the runner is selected to python 
    
    4.	Next, you’ll need to install Flask, load up terminal and type “sudopip3 install flask” this will install flask for you and install pymongo which is sudopip3 install pymongo
    
    5.	 To run the project run the app.py file, you now will be able to view my project in your own IDE.
    
Deploying to Heroku:

    1.	First go to https://dashboard.heroku.com and create an account
    
    2.	Once that is done you will be redirected to https://dashboard.heroku.com/apps, once loaded click on create new app and give the app a name, then hit create app
    
    3.	Next depending on your IDE, if you are using Cloud 9 you won’t need to install Heroku, if not you might have to, on the page you are now on, below it will explain how to install Heroku CLI
    
    4.	After this head on over to your IDE and go to your terminal and type in ‘Heroku login’ and then enter your email and password you just use to create your Heroku account. 
    
    5.	Once this is done use the ‘heroku apps’ command to check if the app you just made is there.
    
    6.	Next in the terminal type ‘git remote add heroku (your URL here)’ you can find your project url in the setting on Heroku. After this to ‘git add .’ to add everything in your IDE, then to a git commit and give it a message of your chose, finally ‘git push -u heroku master’
    
    7.	If your git push failed, it probably because you don’t have a requirements.txt file. To add one, in the terminal type ‘sudo pip3 freeze –local > requirements.txt’ this will create the file and now Heroku will now know what file it needs to install to run the project. Now commit and push the change to Heroku to get your project to work
    
    8.	Finally, to run your project we need to create a profile. Head on over to the terminal and type ‘echo web: python app.py > procfile’ yours might be run.py instead of app.py. now git commit and git push this procfile to Heroku.  To avoid any more errors in the terminal enter ‘heroku ps:scale web=1’.
    
    9.	Now head onto Heroku and go to setting and click on reveal config vars, now enter these configurations IP 0.0.0.0 and PORT 5000
    
    10.	Your project is now fully deployed.
        
        
Credits
Content
    Used materialize https://materializecss.com/ for main layout and styling
    icons came from https://material.io/tools/icons/?style=baseline
    
Media

Acknowledgements

        
        
        
        
        
        
        