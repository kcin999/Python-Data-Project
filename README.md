# Python Data Project
This is a repository for learning baseball data and learning dash and how to visualize it all together. 

This is not yet functional, and is a side project of mine;.

Great site explaining what some of the columns mean: https://baseballsavant.mlb.com/csv-docs

## Things I want to do
* **Long Term**: NPL with search bar to find information about data
* Ability to custom create graphs with the data that I have
    * Line charts or bar charts all within the website / plotly rendering. (Drag and Drop kinda stuff)
    * I think the overall goal of this, is to use my coding ability to 'remove' coding from the website, but still give customizable . We will see how this goes.
* Theme the entire website
    * Dark mode
* Create Database Schema / Diagram. 
    * Possibly use MySQL or ability to toggle SQLite or MySQL
* Make this have the ability to be more than just a baseball website. 
    * But I want to be able to set it up to be able to break apart / pick and choose the pieces to publish if it comes to that. 
    * So like adding stock information / datapoints in a seperate database.
* Predicitive tend lines for mlb data.
    * Figure out what makes a good model, and make it user friendly. 

## Set Up
1. Make sure that Python is installed on your system. This code works and has been tested on Python 3.10, but it may work on older versions, though it is untested. 
2. Run `git clone https://github.com/kcin999/Python-Data-Project.git` in terminal
    * Note: This assumes that git is installed on your system as well.
3. Run `pip install -r requirements.txt` in the terminal where the placed
    * Note: This assumes that pip is also installed with python on your system
4. If you wish to use the Robinhood Database system, then set the following enviroment variables on your system:
    * ROBINHOOD_USERNAME
    * ROBINHOOD_PASSWORD
    * ROBINHOOD_ONETIME_PASSWORD
        * Only set if you are using MFA

## How to run
Run the following command with the root of the project:
```
python app/app.py
```

Navigate to http://127.0.0.1:8050/ in your browser to see the application

## Database Info
Please navigate to the [Database Folder](app/database/) for more information regarding the database

<details>
    <summary>Issues / Things not working yet</summary>
    <h2>Sphnix Documenation</h2>
    <p>
        This code is documenated using Sphinx Standards. If you wish to create the documentation to show in the app, then run the [create_docs.bat](/create_docs.bat) file
        I have the docsite working when commenting out the dash.register_page functions in the subpages
    </p>
</details>
