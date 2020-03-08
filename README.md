# MS4 - xxRelix4U 

link to site here: [xxRelix4U](https://relix4u.herokuapp.com/)

Overview: 

For my milestone 4 project I'm going to create an auction site that will list and sell ancient and legendary relic of our time !  
 
 [![Build Status](https://travis-ci.org/xxkaminaxx/XxRelix4U.svg?branch=master)](https://travis-ci.org/xxkaminaxx/XxRelix4U)

# UX


External user goals :

* To seek and find an artifact.
* To be enlighted to the history and events pertaining to the artifact. 
* To Purchase an artifact listed on this site. 


Site owner/seller goal: 

* To earn money from selling artifacts
* To get user to sign up to site and enable purchaseing as a result. 
* To educate users of the history behind artifacts 

#### User stories :

* As a user i would like to be able to type in a keyword to search for items im interested in. 
* As a user i would like to be able to see the price for an artifact and other details pertaining it to make an informed decision on whether to purchase or not. 
* As a user i would like to be able to bid on/purchase an artifact to potentially aquire said item.
* As a user i would like to be able to learn about the some history or events of the item. 



#### Wireframes:

I hand drew my wireframes and linked them below:

* [Artifact/homepage](https://github.com/xxkaminaxx/XxRelix4U/blob/master/wireframes/artifact%20page.jpg)
* [Cart](https://github.com/xxkaminaxx/XxRelix4U/blob/master/wireframes/cart.jpg)
* [Checkout](https://github.com/xxkaminaxx/XxRelix4U/blob/master/wireframes/checkout.jpg)
* [Login/register](https://github.com/xxkaminaxx/XxRelix4U/blob/master/wireframes/login%26register.jpg)
* [Profile](https://github.com/xxkaminaxx/XxRelix4U/blob/master/wireframes/profile.jpg)

# Features

#### Existing features:

General features:   


Each page has a responsive navigation bar and footer. on the left hand side of the navbar is a logo that when clicked directs user to index.html.
There are call to action buttons on some pages for example on the register.html age theres a link that directs user to login page if they already have an account.



* Back to home button - by clicking the logo on the top lefthand side user can return back to the homepage. 
* Navbar - allows user to navigate through the various pages within app. 
* Search bar - allows user to search for artifact when they type in keyword relating to artifact. 
* Refresh button(Search bar) - This refreshed the search results on the product page.
* stripe payment - allows payment to be made onto pages 
* add quantity / adjust quantity - Enabled user to add items to basket
* Login - Enables user to access there own account make but them. 
* logout - Enables user to sign out of their account. 
* register - Enables user to create an account to access full site features
* reset password -Enables user to change password if it is lost or forgotten in any event. 
* personal username displayed. - When user logins in thre username is displayed in the home.
* admin panel - Enables the use of built-in admin features 
* Back to top button. - takes user back to top of bpage if they have scrolled past a certain point. 
* messages - displays flash messages to give user new infomation for example when loggining in the user will see a message that says "you have logged in "





#### Features left to implement:

I wasn't able to implement the features listed here because at the time of working on this project I only had basic understanding of the framework. There was a moment was where I created the necessary models for these features but in the end I decided to deleted code and abandon this feature because I had ran out of time. 

* Bidding - Enables user to compete for for item by offereing the highest price within a specified amount of time.
* recently viewed items -  Enables user to view the last viewed items. This was going to be displayed in a home page and personal profile.
* Watchlist - Enables user to to store artifacts on there account to recall what they would like to buy. 
* Homepage - This was originally in the project however taken out because it became redundent due to the fact other features weren't going to be included. 
on the homepage I wanted to display most viewed items and recommended items e.g items the user would like. 
* Personal profile page - This was originally in the project however near the end of development I deleted iot because it became redundant. On this page i wanted to displayed the users watchlist
, recently viewed and bought items history. 

# Technologies used: 

Gitpod 

* This was used as my IDE while developing app. 

Bootstrap CDN 

* I used bootstrap to make the app responsive and to provide structuring

HTML

* I used this for each page and to implement templates to load into my app. 

CSS 
 
* I used this to add my own styling to the project. 

Javascript 

*  I used this to add a back to top button and to hide and show the artifact descriptions 

Fontawesome

* I used this to implement unique icon to make the app user friend. 

Google Fonts 

* I used this to implement a unique font.

Python 

* I  used this for backend functionality and manipulation e.g to link the functions and usrl's together in order to traverse through the app. 

mySQL:

* I used this for local database storage of the artifact cards.

PostgresSQL:

* I used this to for database storage when deploying on heroku. This is required when deploying to heroku as taught via code institue videos.

Amazon web services S3 storage bucket :
*  I used this to store and link my static and media files to my deployed website. 
This is because to deploy to heroku i needed to use postgresSQL furthermore postgres will delete my media files because I'm using its free tier version of the database therefore s3 is necessary to store and return media files to display in the project. 


# TESTING 

click [here] (https://github.com/xxkaminaxx/XxRelix4U/blob/master/TESTING.md) to view TESTING.md file.

***
# DEPLOYMENT

#### local deployment: 
I used gitpod to deploy project locally so i'll explain how i did this via gitpod.

* Go to my github repository [here](https://github.com/xxkaminaxx/Xxrelix4U)
* click "clone and download" and then copy the url . 
* Open up your own IDE, I used gitpod.
* Within the terminal type "git clone" then hit space bar and paste the url next it. 
* Hit enter then the file should be loaded and displayed 
* You may need to "cd" into the right folder. e.g " cd XxRelix4U "
* you will need to create an env.py file to store your secret keys in.
* heres an example of what you will need in your env file: 
```
os.environ.setdefault("STRIPE_PUBLISHABLE",
                      "STRIPE_PUBLISHABLE_KEY")
os.environ.setdefault("STRIPE_SECRET",
                      STRIPE_SECRET_KEY")
os.environ.setdefault("DATABASE_URL",
                      "DATABASE_URL_KEY")
os.environ.setdefault("SECRET_KEY",
                      "SECRET_KEY_HERE")
os.environ.setdefault("SITE_NAME",
                      "SITE_NAME_HERE
os.environ.setdefault("EMAIL_ADDRESS",
                      "ENTER_EMAIL_ADDRESS")
os.environ.setdefault("EMAIL_PASSWORD",
                      "ENTER_EMAIL_PASSWORD")

```
* For the stripe keys you will need to register and make an account. Once your account is mad, while on the home tab, there will be a link 
that says " get your test API keys " enter these keys into your env.py file.
* For the SECRET KEY AND SITE NAME these will be found in the settings.py file.
* The email password you will have to choose a gmail account and go to "manage account" then security 
then you need to enable 2 step verification and create a app password. as explained in this video I watched: https://www.youtube.com/watch?v=NdE-Lg2A-zw
Once done enter key into env file. 
* Use this  ```$ pip3 install -r requirements.txt``` command to install  all requirements from requirements.txt file 
* Use ```python manage.py runserver``` to launch code 
* When running django for the first time
 it should create an SQLite3 database file.
 * Next you'll need to create the database schema. Use these commands: 


```
python manage.py makemigrations
python manage.py migrate

```

* Create a superuser with this command  ``` python3 manage.py createsuperuser ``` this will give you access to the admin panel.
* Once the database migrations and superuser are implemented, the existing migrations.py files from each app will configure the datbase schema needed for the project.

#### Heroku 
To deploy project to heroku the following steps were taken:

I created a requirments.txt file so heroku can. I used this command  ```pip3 freeze --local > requirements.txt```

I created a procfile. This will tell heroku what kind of application is being deployed and how to run it. Include this into procfile ```web: gunicorn main.wsgi:application ```

I Created an account on heroku. create app. Then click on the Deploy tab and under "Deployment method" click "connect to github" search for repository.

Then enable automatic deployment.

In the Heroku Resources tab click on the add-Ons section and search for Heroku Postgres. Select the free Hobby level. This will enable you to have a remote database instead of using the local sqlite3 database,
Then update your .env file with your new database-url details.

Scroll up to settings and click "reveal config vars" and enter the postgress secret key

Next to go back to the settings.py file and to connect the remote datbase with the package ```pip3 install dj_database_url ```

At this point you will need to re-build the migrations and create a superuser again to your new remote database use the instructions in the local deployment section above.

#### Amazons storages s3 bucket 

Sign up for a free AWS Amazon account in order to host your staticfiles and mediafiles. This is where 
images will be stored when you create a a new artifaact model. 

Create a new bucket and add these configurations:

Permissions > CORS configuration:

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>

``` 
Permissions > Bucket Policy:


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<N>/*"
        }
    ]
}

```
NOTE ! - on the Resource line above, you'll need to replace replace <N> with your own unique AWS bucket arn details. Keep the /* at the end. example: "Resource": "arn:aws:s3:::my-bucket-name/*"

Next go to the IAM section of AWS.
* Create a New Group and select your existing S3 Bucket details to attach.
* Again within the IAM section create a "New Policy" and a "New User" then link them to the Group you made.
Now in gitpod or your chosen IDE terminal , you should be able to push the static files to AWS using this command:
```python manage.py collectstatic```

your project should be set up for remote deployment :) 

# CREDITS

 #### Code: 
 
  


#### Content : 


#### Acknowledgements : 
During the development of this project because i had very little time left I used alot of the django mini project 
code. So what i mean is as i was learning and implimenting the mini project i was also editing it to what would eventually become my milestone 4. I changed most areas and made it my own, nevertheless I'm acknowledging some of my code will look similar to the mini project.
