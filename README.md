# Climbing Buddy

This website allows climbers in Ireland to find a climbing partner for chosen date and time. Registered users will be able to create a request to look for a climbing partner at chosen time and place.

![Climbing Buddy](static/media_README/mockup.PNG)

:globe_with_meridians:[Live website](https://climbing-buddy-project.herokuapp.com/)

:page_facing_up:[GitHub repository](https://github.com/mateuszniechwiej/Climbing-Buddy)

# Table of Contest

- [UX](#ux)
  - [The Strategy Plane](#the-strategy-plane)
    - [Project Goal](#project-goal)
    - [Site Goals](#site-goals)
    - [User Stories](#user-stories)
  - [The Scope Plane](#the-scope-plane)
    - [Planed Features](#planed-features)
  - [The Structure Plane](#the-structure-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
  - [The Surface Plane](#the-surface-plane)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Database Architecture](#database-architecture)
    - [Differences to design](#differences-to-design)
    - [Imagery](#imagery)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Programmes and Libraries](#frameworks-programmes-and-libraries)
- [Testing](#testing)
- [Code Issues](#code-issues)

- [Deployment](#deployment)
  - [Project Initiation](#project-initiation)
  - [Connecting to MongoDB](#connecting-to-mongodb)
  - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

# UX

## The Strategy Plane

### _Project Goal_

This website project targets the climbing community in Ireland. The primary focus is to allow users to create a request to find a climbing partner and check any climbing events created on this site.

### _Site Goals_

- To provide users with a simple and easily navigated website to help them to create a request to find the correct partner for the climbing day.
- To increase the number of climbing events and allowing participating expanding network of new friends who share the same passion.
- Create a website fully responsive on mobiles, tablets, and desktop devices.

### _User Stories_

1. As a user, I want to understand the purpose of this website.

2. As a user, I want to find an easy navigate website and find all the content.

3. As a user, I want the website to be responsive and allow me to use it comfortably on all size devices(particularly mobiles phones).

4. As a user, I want to be able to register to the website and then create a request to look for a climbing partner.

5. As a user, I want to see if anyone created a request for a climbing partner.

6. As a user, I want to be able to select the requirements I have for a climbing person I'm looking for(skills, equipment and what type of climbing I want to do that day).

7. As a user, I would like to get notified once a person accepted my request.

8. As a user, I want to find about any climbing events taking place.

9. As a user, I want to be able to contact the site owner for any questions or suggestions I might have.

## The Scope Plane

### _Planed Features_

:one: Users able to register.

:two: Allow admin and users to login.

:three: Allow admin and users to create climbing partner search event.

:four: Allow users to read events created by others.

:five: Display Users profile.

:six: Climbing events displayed created by admin.

:seven: Allow users to accept events created by others.

:eight: Allow selecting date and hour for the climbing buddy search event.

:nine: MongoDB database to store information about users and profiles.

:one::zero: Responsive website with a navigation menu and website title.

| -   | Planed Feature                                                     | Importance | Viability/Feasibility |
| --- | ------------------------------------------------------------------ | ---------- | --------------------- |
| 1   | Users able to register                                             | 5          | 3                     |
| 2   | Allow admin and users to login                                     | 5          | 3                     |
| 3   | Allow admin and users to create climbing partner search event      | 5          | 4                     |
| 4   | Allow users to read and accept events created by others            | 4          | 5                     |
| 5   | Display Users profile                                              | 4          | 4                     |
| 6   | Climbing events displayed created by admin                         | 3          | 4                     |
| 7   | Allow users to accept events created by others                     | 3          | 5                     |
| 8   | Allow selecting date and hour for the climbing buddy search event  | 3          | 3                     |
| 9   | Use MongoDB database to store information about users and profiles | 5          | 4                     |
| 10  | Responsive website with a navigation menu and website title        | 5          | 2                     |

## The Structure Plane

### _Addresing users stories_

> As a user, I want to understand the purpose of this website.

A solution to satisfy user requirements:

- Top navigation menu in the Header displaying Home, Login, and Registration links.
- Caption Letters on the background image on the home page with a brief description of what the page purpose is

> As a user, I want to find an easy navigate website and find all the content.

A solution to satisfy user requirements:

- For unregistered users - a menu link for climbing events and registration would be available.

- For registered users additionally -

  - Option to display and create a climbing partner search

  - Display profile information

  - Logout menu link.

> As a user, I want the website to be responsive and allow me to use it comfortably on all size devices(particularly mobiles phones).

A solution to satisfy user requirements:

- Material Design for Bootstrap 5 will be used for this website to ensure all content is displayed correctly.

> As a user, I want to be able to register to the website so that I can create a request to look for a climbing partner.

A solution to satisfy user requirements:

- registration button will be available from the Homepage in the header navigation link.

> As a user, I want to see if anyone created a request for a climbing partner.

A solution to satisfy user requirements:

- for registered users page with climbing requests will be available.

> As a user, I want to be able to select the requirements I have for a climbing person I'm looking for(skills, equipment and what type of climbing I want to do that day).

A solution to satisfy user requirements:

- climber search request form will have options to select:
  - prefered climbing type: sport, traditional or bouldering.
  - equipment provided by the user who makes a request.
  - desire level of skills from the other climber.
  - autocomplete places location input for climbing location.

> As a user, I would like to get notified once a person accepted my request.

A solution to satisfy user requirements:

- once the interested user clicks the `More Info` button from the 'Find Climber' page. The climb_info page where he can press `Contact Climber` details about the climb and have a modal form with session username, email and message to fill out will appear for the user to submit. After submitting the modal form, an email will be sent to the climbing search event creator with the user name and email details of who accepted the request.

- emailjs.com will be used to send mail after accepting the climbing request.

* Example of an email received from user whom is interested in the climb:
![emialjs](static/media_README/emailJS.png)


Comments: Feature implementation: private chat messages between users to be available for each climbing event so users emails don't need to be revealed(Consider solution: Sending private messages using Flask-SocketIO).

> As a user, I want to find about any climbing events taking place.

A solution to satisfy user requirements:

- climbing events created by the admin will be available for both registered and unregistered users.

> As a user, I want to be able to contact the site owner for any questions or suggestions I might have.

A solution to satisfy user requirements:

- an email and/or contact form will be available for any website users

## The Skeleton Plane

### _Wireframes_
[Wireframes](https://xd.adobe.com/view/b3b26688-13e3-4b8a-94fd-98b06524cdf9-e6e1/)

## The Surface Plane

### Design

#### Colour Scheme
* Used Adobe Color to choose the colour pallette.
![Colour Pallette](static/media_README/colours.PNG)

#### Typography

:black_nib:

* Two fonts are used in this project.For most of the headings i used **'Indie Flower'** with *cursive* as a fallback font. A fun handwriting font easy to read with rounded edges. Which was what I was looking for in this project.

* The second font used for this website is **'Oswald'** with *sans-serif* as a fallback font. A readable and interesting font that fits best for body content.

### Differences to design:
After consultation with my mentor and from receiving feedback this are the changes to this project:

1. Navbar changes:
    - changing locations of the link to left side and adding logo on the right side on navbar
    - hover on links adding underline only now.
    - relocating links: to add event and add climb to other pages
2. Footer - email link icon replaced email address as design improvement
3. Events page:
    - 2 events cards per row with images showing up to 4 events card per page
    - search bar added for better user experience
    - add pagination to event page to show up to 4 events per page
    - add climb moved from navbar beside search bar as a button for better UX
4. Register page:
    - add confirm password functionality
    - add redirect to login page if already registered for better user experience
5. Login page:
    - add link to registration page for better user experience
6. Finding Climber:
    - page renamed from Climbing Buddy for better meaning
    - filter climbs added to allow user filter by date,type of climbing and location
    - add climb moved from navlink
    - `Accept Climb` button replaced with `More Info` to redirect users to new page where they can read a message from user and send message to that user.


### Database Architecture
* **MongoDB** non-relational database is used to store data for this project
* Database design for this project is based on three collections: 
    * __*users*__(stores: users name and email)
    * __*climbs*__(stores: climbs events(requests) raised by registered users)
    * __*events*__(stores: climbing events raised by _**admin**_)


![MongoDB Database Desgin](static/media_README/database.png)

### Imagery

Images for this project 
- [Background Image by Patrick Hendry](https://unsplash.com/photos/WrCvD2Cgb4c)
- [Outdoor Climbing Image by PatrickHendry](https://unsplash.com/photos/w5hNCbJfX3w)
- [Indoor Climbing by Pavel Danilyuk](https://www.pexels.com/photo/landscape-man-people-woman-7591312/)
## Features

### Existing Features

:one: The landing page displaying information about the website's purpose.

:two: Events page displaying three events per page.

:three: Create an events page available for the admin.

:four: Register and login functionality.

:five: Climbing events displaying three climbs per page.

:six: Add Find Climber request event available for all registered users.

:seven: Profile page with username name and email.

:eight: Message climber form using EmailJS functionality.

:nine: Email link on all pages to contact the website owner for any information needed.

:one::zero: Places Autocomplete by Google(a feature of Places library in the Maps JavaScript API) to look for locations in Ireland and the Uk only.

:one::one: Mobile responsive design.

:one::two: Error page to display error messages with website background.

:one::three: filter climbs functionality searched by categories selected.

:one::four: searched bar on events page to look for phrases in the events text.

:one::five: Google _**Place Autocomplete**_ functionality for each location input field in this project.

### Future Features

:one: Private chat messages between users to be available for each climbing event so users emails don't need to be revealed.

:two: A gallery page to allow the user to add photos from events and climbs.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://pl.wikipedia.org/wiki/JavaScript)
    - emailjs for sending message between users
    - places autocomplete for location input field for better user experience
    - flatpick for date picker

* [Python](https://www.python.org/)
    - Python Modules used in this project can be found in the requirements.txt project file)

## Frameworks, Programmes and Libraries
* [mdbootstrap](https://mdbootstrap.com/) - Material Design for Bootstrap 5 used for layouts, styling and custom components such as forms, navigation bar or modals.
* [emailjs](https://www.emailjs.com/) - to allow users to respond to climbing request by sending an email message.
* [JIRA](https://www.atlassian.com/software/jira) - project management tool to organize workflow.

* [Adobe Photoshop Express](https://photoshop.adobe.com/?promoid=SYBNM1DC&mv=other) - To crop the full-page background image.
* [Adobe Xd](https://www.adobe.com/ie/products/xd/wireframing-tool.html#:~:text=Adobe%20XD%20is%20a%20powerful,all%20in%20one%20design%20tool.) - to create wireframes

* [Canva](https://www.canva.com/) - Canva was used to create logo for the website.
* [Lucidchart](https://www.lucidchart.com/) - used to create Database design diagram.
* [JPEG-OPTIMIZER](http://jpeg-optimizer.com/) - optimized the size of images used in this project.
* [techsini](https://techsini.com/) - to generate website mock-up.
* [Google Fonts](https://fonts.google.com/) - used to import fonts 'Indie Flower' and 'Oswald' for this project.
* [Font Awesome](https://fontawesome.com/) - for social media links and forms icons.
* [MDBootstrap](https://mdbootstrap.com/) - Material design for bootstrap is used for layouts, styling and responsiveness.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Flask Python micro framework is used in this project to help develop the application.
* [Heroku](https://heroku.com) - Heroku was to deploy and host the live website.
* [MongoDB](https://www.mongodb.com/) - MongoDb document-oriented database used to store information about users,events and climbs.
* [Visual Studio Code](https://code.visualstudio.com/) - used for developing this website and commit the project to GitHub repository.
* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - used to debug the styling issues, test the website responsiveness  and to make sure colour contrast is correct.
* [Autocomplete Places Google API](https://developers.google.com/maps/documentation/places/web-service/autocomplete) - provides a fast and easy to use address search autocomplete functionality for locations fields input.
* [Flatpickr](https://flatpickr.js.org/) - lightweight DateTime picker used to select dates in this project.
* [Github](https://github.com/) - Github as the hosting site was used to store the source code of this website.
* [Git](https://git-scm.com/) - used Git to commit and push code to the GitHub repository.
* [Favicon](https://favicon.io/) - to create a favicon for this Website.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse) - as a part of the chrome dev tool was used to improve the quality of the web page.

## Testing

Testing :point_right: [TESTING.md](TESTING.md)

## Code Issues
1. Email.js functionality issue:
Not sending emails when followed the steps from emailjs documentation after moving climber modal contact form to "contact climber" page.

This was the initial code: (with:`onsubmit="return sendMail(this);` in html form):
```function sendMail(acceptForm) {
     acceptForm.preventDefault();
        emailjs.send("gmail", "climbing_buddy", {
            'user': acceptForm.name.value,         
            'user_email':   acceptForm.email.value,
            'other_user': acceptForm.creator.value,
            'other_email': acceptForm.receiver.value,
            'message': acceptForm.message.value,
        })
         .then(
            function() {
                document.querySelector('.response').innerHTML = "Your message was sent!";
            },
            function() {
                document.querySelector('.response').innerHtml = "There was an error to send your message. Try again later..."
            }
        );
    return false;
 }
 ```
**Understanding the problem** - was not sure what was causing this problem.

**Solution** - I needed to change the approach with help from Tutor support by:
*Getting the form in the script file, and stopped the page from reloading.*

2. Some modals not displaying borders and lack of response message display confirming message send by email.js(however the message was send by email.js at that time):

**Understanding the problem** : The issue was caused by repeating Id's on the same html page in the modal forms.

**Solution**: Moving Modal to another page and passing single climbing id by introducing `More Info` button to the climb event card.

3. Modal opening on page load in contact climber page:

**Understanding the problem**: Probably issue caused by MDBootstrap framework as steps taken from mdbootstrap documentation didn't work

**Solution** - introduce `CONTACT CLIMBER` button to open the modal.

4. Manipulator js error in the console on contact climber page

**Understanding the problem**: Probably issue caused by MDBootstrap framework

![console error](static/media_README/consoleError.PNG)

**Solution** - Not resolved

## Deployment

### Local Clone
1. Navigating to the GitHub [Repository](https://github.com/mateuszniechwiej/Climbing-Buddy)
2. Click on Code green button.
3. Under the Clone section, copy the URL from the HTTPS : 

![Clone](static/media_README/clone.png)

5. Use the IDE of choice to open the terminal.

6. Use git clone command followed by the copied URL.

7. A clone of the project will now be created locally on your machine.

### Create a Virtual Environment(VSCode)
__(You need to have installed Python extensions and Python version 3 before taking following steps )__
1. On the the local system create project folder e.g MS3
2. In that folder use(for Windows) the command: `python -m venv venv`
3. Select and activate an environment (To select a specific environment, use the `Python: Select Interpreter` command from the `Command Palette (Ctrl+Shift+P)`.

More info: [VSCode docs](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)

### Connecting to MongoDB
1. Logged to MongoDB account.
2. Within the "Cluster1" tab selected, I clicked on "Connect".

![Connect](static/media_README/connect.png)

3. Then selected "Connect your application".

![ConnectApp](static/media_README/connect_app2.png)

4. Select _Python_ version 3.6 or later.
5. Copy _connection string_ and then paste it to env.py

![mongoDB](static/media_README/mongodb.png)

6. Finaly create an instance of PyMongo and pass the application to that instance.
* Like:  `mongo = PyMongo(app`)

### Heroku Deployment

Preparing Local workspace for Heroku:
1. Creating a *__requirements.txt__* file(Required for the Heroku to know which apps need to be installed for the app) by typing in the CLI: :
`pip freeze --local > requirements.txt`

2. Creating *__Procfile__* file to declare what commands are run by the application's dynos on the Heroku.
Type in file `web: python app.py` and save.

Create Heroku application:
1. Create Heroku account.
2. Press `New` button. 
2. Select `Create a new app`.
3. Enter the app name.
4. Select region.
5. Under `Settings`, __click__ `Config Vars` to add Configuration Variables from the env.py file.
6. In your CLI install Heroku by typing `npm install -g heroku`  
7. Select `Deploy` option.
8. Under `Deployment method` select the __GitHub__ option.
9. Select Automatic deploys from the main branch and select `Deploy Branch`.
10. Click `Open App` button located in the top-right corner of your Heroku account.

## Credits

### Code

* [MBBootstrap libary](https://mdbootstrap.com/) used to create a responsive design and how add focus message field in modal.
* [MDBootstrap](https://mdbootstrap.com/snippets/standard/grzegorz-bujanski/2852722#css-tab-view ) - to change default blue for form-outline. 
* [Places Autocomplete by Google](https://developers.google.com/maps/documentation/places/web-service/autocomplete) - to set up correctly location autocomplete functionality.
* <a href="https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9"> pagination flask</a> - to learn how to make pagination using flask
* [flatpickr examples](https://flatpickr.js.org/examples/) - to learn how to set up date picker.
* [Stack Overflow](https://stackoverflow.com/questions/23968961/css-how-can-i-make-a-font-readable-over-any-color) - how to make headings more visible on the background image


## Acknowledgements
* My mentor, **_Maranatha Ilesanmi_** for advice, guidance and support on this project.
* Sean and Igor from **Tutor Support** - for helping to fix the issues with my modals and email.js functionality.
* **Slack Community** - for feedback on my project.
* **My friends and family** - for giving feedback on my project and testing this website.