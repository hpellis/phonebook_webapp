from flask import Flask, render_template, request
from engine import Phonebook

app = Flask(__name__)
phonebook = Phonebook()


@app.route('/')
def index():
    return render_template("layout.html")


@app.route('/person_search')
def person_search():
    return render_template('person_search.html')


@app.route('/person_search_result', methods=['GET', 'POST'])
def person_search_result():
    x = Phonebook()
    search_term = request.form['person_name']
    result = x.find_person(search_term)
    return render_template('person_search_result.html', result=result)


@app.route('/business_search')
def business_search():
    x = Phonebook()
    categories = sorted([i[0].strip() for i in list(set(x.get_categories()))])
    cities = sorted([i[0].strip() for i in list(set(x.get_cities()))])
    return render_template('business_search.html', categories=categories, cities=cities)


@app.route('/business_search_result', methods=['GET', 'POST'])
def business_search_result():
    x = Phonebook()
    name = request.form['business_name']
    category = request.form['business_category']
    location = request.form['business_location']
    result = x.find_business(name, category, location)
    return render_template('business_search_result.html', result=result)    
    
   
@app.route('/view_all_businesses')
def all_businesses():
    x = Phonebook()
    businesses = x.get_all_businesses()
    return render_template('view_all_businesses.html', businesses = businesses)


@app.route('/view_all_people')
def all_people():
    x = Phonebook()
    people = x.get_all_people()
    return render_template('view_all_people.html', people=people)


if __name__ == '__main__':
    app.run()
