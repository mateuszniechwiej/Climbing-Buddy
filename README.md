# Climbing Buddy

This website allows climbers in Ireland to find a climbing partner for chosen date and time. Registered users will be able to create a request to look for a climbing partner at chosen time and place.

# Table of Contest

- [Project Workflow](#project-workflow)
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
    - [Imagery](#imagery)
- [Features](#features)
  - [Existing Features:](#existing-features)
  - [Future Features:](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Programmes and Libraries](#frameworks-programmes-and-libraries)
- [Testing](#testing)

  - [Testing Plan](#Testing-Plan)
  - [Testing Results](#Testing-Results)

- [Deployment](#deployment)
  - [Project Initiation](#project-initiation)
  - [GitHub Pages](#github-pages)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

# UX

## The Strategy Plane

### _Project Goal_

This website project targets the climbing community in Ireland. The primary focus is to allow users to create a request to find a climbing partner- and check any climbing events created on this site.

### _Site Goals_

- To provide users with a simple- and easily navigated website to help them to create a request to find the correct partner for the climbing day.
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
  - dropdown list for climbing location.

> As a user, I would like to get notified once a person accepted my request.

A solution to satisfy user requirements:

- solution not yet found:question:

Considered solutions:

:hash: Send automatic email to user once his request was approved.

:hash: Display participating(in the request) users emails.

> As a user, I want to find about any climbing events taking place.

A solution to satisfy user requirements:

- climbing events created by the admin will be available for both registered and unregistered users.

> As a user, I want to be able to contact the site owner for any questions or suggestions I might have.

A solution to satisfy user requirements:

- an email and/or contact form will be available for any website users

## The Skeleton Plane

### _Wireframes_
