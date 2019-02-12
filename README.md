# Phonebook Web App

This is an online phonebook which can be used to search for (invented) businesses or individuals who appear in the database. 

## Development
I used SQLite to create the database used in this project. I then populated the tables in this database with randomly-generated data for individuals and businesses. I used the postcodes.io API to convert postcodes into longitude and latitude datapoints, saving geolocation data into a third table. (This was used in a command-line version of the app to calculate the distance between search and result locations.)

The search engine functionality is written in Python, and uses SQL queries to find entries in the table that match search terms. 

The app is accessible via a front-end interface, which uses Flask to receive user inputs from HTML forms and to send search results to HTML tables. Users can search for individuals by name, or for businesses by name, type and/or locations. Alternatively, the entire database can be displayed and JQeury's DataTable search functionality can be used to filter data. 

## Technologies
* Python
* SQL
* SQLite
* Flask
* HTML
* CSS
* Bootstrap


## Installation

Clone the repository.

```$ git clone https://github.com/hpellis/phonebook_webapp```

Navigate to the directory. 

```$ cd phonebook_webapp```

Install Flask.

```$ pip install Flask```

Run the app file.

```$ python phonebook_webapp.py```

Navigate to the local host address in your browswer to see the app running.


![image of table](/final_images/table.png?raw=true "Table")


![image of home page](/final_images/home_page.png?raw=true "Home Page")


![image of results page](/final_images/results_page.png?raw=true "Results Page")
