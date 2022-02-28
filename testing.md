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

## Validation
* HTML code was vaildated through [WC3 HTML Markup validator](* HTML code was vaildated through [WC3 HTML Markup validator](https://validator.w3.org/nu/) and passed.
* CSS code was vaildated using [WC3 CSS Validation](https://jigsaw.w3.org/css-validator/) and passed.
* JS code was validated using [JSHint](https://jshint.com/)) and passed.
* CSS code was vaildated using [WC3 CSS Validation](https://jigsaw.w3.org/css-validator/) and passed.
* JS code was validated using [JSHint](https://jshint.com/)

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
|Ability to register for an account | When clicking the Sign up the user will be directed to a form to register for an account with a unique username and password | Click on sign up and see if the correct form is provided | When user clicks on sign up the user is redirected the the correct form | Pass |
| Form sends error message if the username is already taken | Form will send a flash message to user if username is already taken and suggest user try a different username | Input a username that already exists into the form and submit to test message | When a username that already exists is input a message is given to user to tey again | Pass ||


#### Log in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|Ability to log into an existing account | When clicking the Log In the user will be directed to a form to input their user name and password | Click the log in button to check the correct form is loaded for the user | When user click login they are directed to the correct form to fill in their details | Pass |
| Access to User Profile when correct user credentials are input | When user inputs correct username and pass word the user is then redirected to the Profile page | Input correct details for user and submit form | With correct details input and submitted the user is redirected to the Profile page | Pass |
| Incorrect details are falgged to user | If user submits invalid information such as wrong username/ password this is flagged to the user | Incorrect username / password input to form | When wrong information added to form the user is given a message to say that the username/ password was incorrect and to try again | Pass ||

[Back to contents](#contents)

### Yarns Page

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|Yarns page shows all yarns with their reviews | The page loads all yarn reviews on the site | click the Yarns link and the page loads with all yarns and their reviews | Pass||

[Back to contents](#contents)

### Adding Yarn

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Ability for user to add a Yran to the library | The user is directed to a form to fill in the details of a new yarn | Click the Add Yarn Link | User is redirected to add yarn form | Pass|| When the user has added the information to the form and clicked complete the yarn is added to the Yarns page for all users to see | Fill in the form and submit it and check that the new yarn is added to the Yarns page | Pass || 

### Editing a Yarn

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Ability for user to edit a yarn that they have alredy reviewed | When clicking the edit button the user will be redirected to the edit yarn page | Click the edit button on the profile page | the edit button passes the user to the edit yarn page | Pass|
| The user can edit the deatils of a yarn tat they have already reviewd using the form on the edit yarn page | Filling in the ofrm and submitting the changed will update the yarn on the all yarns page | Edit a yarn and check that the information is updated | Pass||

### Deleting a Yarn

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Ability for user to delete a yarn that they have reviewed | The user has the option to delete a yarn from their profile | Click the Delete button on the profile page | Yarn is deleted and the user is redirected to the Yarns page | Pass||

### User Profile

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Ability for user to view the yarns that they have previously reviewed | Click onto Profile page and check that users yarn reviews are visible | Yran reviews for user can be viewed | Pass|| A user can edit a review that they have previuosly submitted | Clicking in the edit button should give the user access to the edit yarn function | The button take the user to the Edit Yarn page | Pass ||  A user can delete a review that they have previuosly submitted | Clicking in the delete button shold allow the user to delete a yarn | The button deletes the yarn | Pass ||

## User Stories

| As a User        | I want to...           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| User | easily navigate the site | Check that all navigation links work and clearly visible | tested navigation functions | Pass |
| User | register for an account| Check that registration function is working correctly and that a new user can register for an account | tested registration function | Pass |
| User | log in and out of the site | Check that the login and log out functions are working as expected | Log in and log out functions have been tested and are working correctly | Pass |
| User | add a review of a yarn that I have worked with to help other crafters| Check that the add yarn function is working and that new yarns are showing on the main yarns page | the add yarns function has been tested as well as the yarn page ensuring that the yarn informations is showing in the correct format | Pass |
| User | edit yarns I have reviewed | Check that the edit yarn function is working correctly and that the updated information is showing on the main yarns page | the edit yarn function has been tested and is working correctly | Pass |
| User | delete a yarn I have previously reviewed | Check that the delete yarn function is working correctly and thata yarn is no longer showing on the main yarns page | the delete yarn function has been tested and is working correctly | Pass |
## Responsivness

### Wave
The site was inspected for accessibility using the [Wave Browser Extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) and changes made to HTML following this inspection. 

### Lighthouse
All pages were put through Lighthouse and the scores were all very good, I could still work on labelling a little more consistently.