# Baseball
This is a repository for learning baseball data and learning dash and how to visualize it all together

Great site explaining what some of the columns mean: https://baseballsavant.mlb.com/csv-docs

## Things I want to do
* **Long Term**: NPL with search bar to find information about data
* Ability to custom create graphs with the data that I have
    * Line charts or bar charts
* Theme the entire website
    * Dark mode
* Create Database Schema / Diagram. 
    * Possibly use MySQL or ability to toggle SQLite or MySQL
* Make this have the ability to be more than just a baseball website. 
    * But I want to be able to set it up to be able to break apart / pick and choose the pieces to publish if it comes to that. 

## Set Up
1. Make sure that Python is installed on your system. This code works and has been tested on Python 3.10, but it work on older versions, though it is untested. 
2. Run `git clone https://github.com/kcin999/Baseball.git` in terminal
    * Note: This assumes that git is installed on your system as well.
3. Run `pip install -r requirements.txt` in the terminal where the placed
    * Note: This assumes that pip is also installed with python on your system

## How to run
Run the following command with the root of the project:
```
python app/app.py
```

Navigate to http://127.0.0.1:8050/ in your browser to see the application

## Database Info
Please navigate to the [Database Folder](app/database/) for more information regarding the database

## Sphnix Documenation [Not-Working Yet]
This code is documenated using Sphinx Standards. If you wish to create the documentation to show in the app, then run the [create_docs.bat](/create_docs.bat) file

## Things I need to get working
* Sphinx documenation, or some kind of documenation. 
    * I have the docsite working when commenting out the dash.register_page functions in the subpages
