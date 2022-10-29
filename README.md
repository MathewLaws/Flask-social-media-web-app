# Flask-social-media-web-app
Social media web app made with python, flask, bootstrap and SQL Alchemy

![flask_img3](https://user-images.githubusercontent.com/93098734/198849376-f68958ab-ab7b-4b55-b571-9d4431ce57f7.png)

First, I made a flask app and set a secret key to secure the cookies and session data of the 
website, next I made a base page which had the navbar and styling using CSS bootstrap. I then 
made a simple login page which extended off the base page using jinja to include the navbar 
and then I made some input fields for email and password and applied the same concept to make 
a sign-up page. Once these templates were made, I created a database using SQLAlchemy which 
is an orm (Object Relational Mapper) used to make databases in object-orientated languages, 
I made the database by first making a class called “User” which inherits from db. Model 
(the object used to initialize the database) next I created 4 different columns, one for ID 
which is the primary key and increments after every user, one for name, one for email and 
one for password. After the model of the database is made, I gave it the name “Accounts.db” and 
checked if there was already a database in the directory, if not it is created in the working 
directory.

Following on from the database I created some routes to route the user to the different pages 
when the navbar elements were clicked for example when the user accesses the sign-up page, a 
“GET” request is sent to the server and a function is ran to render the “/sign-up” template otherwise 
if the user is already on the sign-up page and he/she enters valid details in the required input 
fields then clicks the submit button, a “POST” request is sent to the server and the values are 
taken out of the fields and ran through numerous checks such as if the password is less than 6 
characters or the user already exists in the database. If the details are valid the password is 
hashed using “sha256” so people cannot decrypt passwords to text format and once the password is 
hashed then the name, email and password are passed into the User class and the user is assigned 
to the variable “new_user”, and it is then committed to the database.

After the user creates an account they are redirected to the home page which is blank for now, i also used the flask-login module which allows the program to remember a user’s 
account on a device so when the site is refreshed, the user is still logged in which improves the 
user experience as they do not have to constantly type their username and password out. furthermore I used 
this module inside the base page using jinja to put some python code inside my html to check whether 
the user is authenticated and if so only display logout in the navbar otherwise if the user is not 
authenticated only display login and sign-up, this prevents the user from trying to logout of an 
account which they are not logged into and potentially raising an error. Additionally, I used the login 
manager module to put the decorator “@login_required” to prevent users from accessing the homepage 
if they are not logged in.

Future Development Ideas

I would like to further develop this so that the user gets access to something after they have logged in for example their notes, art, reminders etc
I would like to implement email validation for example an email would be sent to the email provided by the user and then the user would click a link to validate the email
I would like to make it responsive so mobile users can use the website

What I Learned

I have learned the basics of web development using frameworks like Django and Flask
I learned how to communicate with web browsers and servers using http through get and post requests for example when I needed to get the users username and password out of the text fields using a post request
I have learned more about databases using libraries such as sqlalchemy and sqlite3
I have learned more about cookies and security for example hashing the passwords from string format
Form handling and validation of data
