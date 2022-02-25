# Testing

## Contents 
* [Code Validation](#validation)
* [Functionality](#functionality)
* [Home Page](#homepage)
* [Navigation](#navbar)
* [Registration/ Login](#registration-and-login)
* [Yarns Page](#yargs-page)
* [Adding a Yarn](#adding-yarn)
* [Editing a Yarn](#editing-yarn)
* [Deleting a Yarn](#deleting-yarn)
* [User Profile](#user-profile)
* [User Stories Testing](#user-stories-testing)
* [Responsivness](#responsivness)
* [Wave](#wave)
* [Lighthouse](#lighthouse)
* [Conclusions](#conclusions)


## Functionality
### Homepage

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Hero Image clear and intro to site  | Clean image and intro to site visible | View home page | Hero image and intro text clear to user | Pass |

[Back to contents](#contents)

### Navigation
#### All users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Link to sign up option  | button and link on the homepage to sign up  | View home page, click button and sign up for an account | Button is clearly visible and when clicked takes user to the sign in page where an account can be created | Pass |
| Link to login option visible on home screen | Button and link on the homepage for a user ro login to their account. | View home page and click button to login to account | Button is clearly visible and when clicked takes the user to the login page where they can access their account | Pass |

#### Logged in users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Link to Yarns Page | There is a link to the Yarns page in the nav bar when user is logged in | Check that link is visible and directing user to correct page | When the Yarns link is clicked it takes the user to the main yarns page were all yarn reviews are available to view | Pass|| Link to Add Yarn in navbar when user is logged in | Check that link is visible and directing user to correct page | When the link is clicked the user is redirected to the Add Yarn page | Pass || Link to Profile page | There is a link in the nave bar for a user to view their profile | Clicking on the link redirects the user to thier user profile page | Pass|| Log Out Button | There is a button in the navbar that the user can log out from the site with |  Clicking this button logs the users out | Pass||

[Back to contents](#contents)

### Registration and Login
#### Registration

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|Ability to register for an account | When clicking the Sign up the user will be directed to a form to register for an account with a unique username and password | Pass || Form sends error message if the username is already taken | Form will send a flash message to user if username is already taken and suggest user try a different username | Input a username that already exists into the form and submit to test message | Pass ||


#### Log in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|Ability to log into an existing account | When clicking the Log In the user will be directed to a form to input their user name and password | Pass || Access to User Profile when correct user credentials are input | When user inputs correct username and pass word the user is then redirected to the Profile page | Input correct details for user and submit form | With correct details input and submitted the user is redirected to the Profile page | Pass || Incorrect details are falgged to user | If user submits invalid information such as wrong username/ password this is flagged to the user | Incorrect username / password input to form | When wrong information added to form the user is given a message to say that the username/ password was incorrect and to try again | Pass ||

[Back to contents](#contents)

### Yarns Page

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|Yarns page shows all yarns with their reviews | The page loads all yarn reviews on the site | click the Yarns link and the page loads with all yarns and their reviews | Pass||

[Back to contents](#contents)

### Adding Yarn

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |