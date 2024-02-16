# DIAREAM: A VIRTUAL DIARY TO WRITE YOUR DREAMS


## Demonstration Video:
https://youtu.be/LaUOWwrwOSc


## Description:
Diaream is an online, account based diary application for people who want to keep a virtual diary that they can bring to and access from everywhere, instead of a handwritten one.


## How to Use Diaream:
- First of all, we need to go inside the project folder on our terminal and execute `flask run` command.

- When we run the app and click the link, we first encounter a log in page. If we have an account, we immediately can log in and start to write in Diaream. If we don't, we have to click `Create A Diaream Account` located at the menu above and create one for us.

- On `Register` page, we have to provide a username, a password and type the password again and they should match. If we don't meet those criteria, the app won't allow us to create an account and will return an apology text based on what we are missing.

- After we successfully created our account, we will be redirected to log in page where we can log in with our own username and password. If we don't type both correct username and correct password, we can't log in but find an apology text again.

- After we logged in, we will be in `Your Diaream` page which shows the diary pages (or logs) in table format that we have written on the app so far. If we are a new user or haven't wrote anything before, this page will be empty.
 
- In order to 'write a page' in our Diaream, we need to click `Write in Your Diaream` on the menu tab. There, we will see a calendar to choose the day we want to write for, a title box, a text box that we can expand and write anything, and also a URL box in case of we would like to add links of pictures and videos that are related to the day. Choosing a date and writing a title and text are essential, so we can't save the page unless we fill those areas.

- After we save it, we immediately will see our new diary page (or entry) listed on `Your Diaream` page. When we are done with adding pages into Diaream, we can log out clicking `Log Out` on the menu tab.


## Languages & Frameworks used in Diaream:
- **Python** (for routing, returning apology texts, inserting into and executing from the database)

- **SQL** (for storing users and diary pages)

- **Flask** (for running the application)

- **HTML + Jinja Syntax** (for templates)

- **CSS** (for styling)

- **Bootstrap** (for page layout, menu tab and table)


## Files:
***app.py:*** Contains `@app.route`s for index, log in, log out, register and diary pages. Returns an apology considering what's wrong if the user doesn't fill requested areas or provide correct information. Also connects the SQL database to the app.

***helper.py:*** Contains declaration for `apology()` as well as an `escape()` function for escaping special characters in apology texts. Also declares `login_required()` function.

***diary.db:*** The database of the application where users and their diaries are stored. Contains two tables: "users" and "diaries". Here's the schema of the database:
- CREATE TABLE users ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL );
- CREATE TABLE sqlite_sequence(name,seq);
- CREATE UNIQUE INDEX username ON users (username);
- CREATE TABLE diaries ( id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, title TEXT NOT NULL, description TEXT NOT NULL, img_url TEXT, FOREIGN KEY(user_id) REFERENCES users(id) );

***requirements.txt:*** Describes the packages used in the app.

***layout.html:*** Where the main HTML code is stored and all other template files extend from thanks to Jinja. Contains the app's title, header and menu tab, and footer block.

***login.html:*** The user is redirected to this page as soon as they run the app if they are already not logged in. Contains a `div` for welcoming the user, and a `form` to request username and password with a Log In button.

***register.html:*** Where the user can create an account for the app. Contains a `form` to request a username, a password and the matching password with a Register button.

***index.html:*** The user is redirected to this page if they are logged in. This page shows the user's previous diary logs with date, title, description of the day, and URLs if there is any. It contains a table designed with Bootstrap.

***diary.html:*** Where the user can add a new diary log (or page) to their diary. Contains a `form` to request date of the day, title for the day, a text for describing events of the day and URLs if the user wants to include, with the "Save My New Diaream Page" button located below.

***apology.html:*** Specifies the layout of apology texts.

***styles.css:*** Specialized styling for the app. Specifies fonts, sizes and colors for the header, the subheader, the menu, the "Diaream" text, apology texts, submit buttons and the table.
