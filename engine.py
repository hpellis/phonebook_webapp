from sqlite3 import connect
from os.path import exists


class Phonebook():
    
    def __init__(self):
        self.db_path = 'static/db/phonebook.db'

    def check_db(self):
        if exists(self.db_path):
            return True
        else:
            return False

    def connect_db(self):
        try:
            if self.check_db():
                self.connection = connect(self.db_path)
                self.c = self.connection.cursor()
            else:
                print('Database does not exist')
                return None
        except:
            print('Failed to connect to database')

    def query_db(self, query, params=None):
        try:
            self.connect_db()
            if params:
                self.c.execute(query, params)
            else:
                self.c.execute(query)
            self.results = self.c.fetchall()
            self.connection.close()
            return self.results
        except Exception as e:
            print(e)

    def get_categories(self):
        try:
            query = "SELECT business_category FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def get_cities(self):
        try:
            query = "SELECT address_line_2 FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def get_all_businesses(self):
        try:
            query = "SELECT * FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def get_all_people(self):
        try:
            query = "SELECT * FROM people;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)



    def find_business(self,business_name=None, category=None, location=None):

        if business_name and category and location:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(business_category) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (business_name,category,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif business_name and category:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(business_category) LIKE UPPER('%%%s%%')" % (business_name,category)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif business_name and location:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (business_name,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif category and location:
            try:
                query = "SELECT * FROM business where UPPER(business_category) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (category,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif business_name:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%')" % (business_name)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif category:
            try:
                query = "SELECT * FROM business where UPPER(business_category) LIKE UPPER('%%%s%%')" % (category)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif location:
            try:
                query = "SELECT * FROM business where UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)
        else:
            self.results = [('Nothing Found')]
            return self.results
        
    def find_person(self, person_name=None):
        if person_name:
            try:
                query = "SELECT * FROM people where UPPER(last_name) LIKE UPPER('%%%s%%')" % (person_name)
                self.result = self.query_db(query)
                return self.result
            except Exception as e:
                print(e)

