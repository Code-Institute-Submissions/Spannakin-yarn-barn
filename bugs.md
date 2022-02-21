# Bugs

## Registration/sign in function
### The Problem
When writing this function its initially wouldn't work despite the Python code being correct after searching through the code.
### The Fix
With the help of a Tutor as second set of eyes we found that the password in the MONG_URI was not working so I reset the password for the admin and linked it up again. After this the registration function worked correctly and new users were saved to the database.

## Login function
### The Problem
The login function was not redirevting through to the profile page.
### The Fix
This was due to an error in my coding where I had forgotten to pass in the username perameter to the redirect function. It now works fine.

## Adding a new yarn
### The Problem
Whilst the function was working the yarn producer name was not pulling through from the database.
### The Fix
On closer insepction of my code I found that I had misspelt the key name so corrected this and then all the infromation was moving to and from the database correcty.

## Navbar
### The Problem
Hamburger icon was not working.
### The Fix
This was due to an error in the javascript that I had written for it I had passed the element the wrong id, once this was corrected then the function workd.
This then threw another glitch as it was showing an error on the home page where the burger was not present as such I wrapped the function within an if statement so that the function could only be called whe the burger was present on the page.

## Heroku app not connected to Database
### The Problem
During testing it came to light that the Heroku app was not connected to the Mongo database this was probably due to the earlier error with the Mongo URI in the registration function.
### The Fix
To over come this I re-entered the details needed into the config vars and the app and database are now able to connect.