# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:14:30 2019

@author: harri
"""

import sqlite3
import json 
import requests

def connect_database():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    return conn, cursor


#creating and populating business table        
def create_business_table():
    conn, cursor = connect_database()
    cursor.execute('CREATE TABLE IF NOT EXISTS business (business_name TEXT, business_category TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, telephone_number REAL, )')
    conn.close()
     
with open('business_database_json.js') as f:
    business_data = json.load(f)


def business_data_entry():
    conn, cursor = connect_database()
    for item in business_data:
        values_list = list(item.values())
        cursor.execute('''INSERT INTO phonebook_business(business_name, business_category, addressline1, addressline2, addressline3, postcode, telephone_number)
                  VALUES(?,?,?,?,?,?,?,?)''', (values_list))
        conn.commit()
        conn.close()


#creating and populating person table  
def create_person_table():
    conn, cursor = connect_database()
    cursor.execute('CREATE TABLE IF NOT EXISTS phonebook_personal (first_name TEXT, last_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, x_coord REAL, y_coord REAL)')
    conn.close()
    
with open('personal_database_json.js') as f:
    person_data = json.load(f)

def personal_data_entry():
    conn, cursor = connect_database()
    for item in person_data:
        values_list = list(item.values())
        cursor.execute('''INSERT INTO phonebook_personal (first_name, last_name, addressline1, addressline2, addressline3, postcode, country, telephone_number)
                  VALUES(?,?,?,?,?,?,?,?)''', (values_list))
        conn.commit()
        conn.close()


# creating and populating location table
def create_postcode_table():
    conn, cursor = connect_database()
    cursor.execute('CREATE TABLE IF NOT EXISTS postcodes (postcode TEXT, longitude REAL, latitude REAL)')
    conn.close()

def get_postcodes():
    conn, cursor = connect_database()
    cursor.execute('''SELECT postcode
    FROM phonebook_business''')
    postcode_data=c.fetchall()
    conn.close()
    list_postcodes = [item[0]
    for item in postcode_data]
    return list_postcodes

def api_convert(list_postcodes):
    endpoint="https://api.postcodes.io/postcodes"
    payload={"postcodes":list_postcodes}
    result = requests.post(endpoint, json=payload)
    postcode_result = result.json()['result']
    return postcode_result 
    
    
def extract_long_lat(postcode_result):
    long_lat_list = []
    for item in postcode_result:
        postcode = item['query']
        try:
            longitude = item['result']['longitude']
            latitude = item['result']['latitude']
            print(longitude)
            print(latitude)
        except:
            longitude = 0
            latitude = 0
        new_data=[postcode,
                  longitude,
                  latitude]
        long_lat_list.append(new_data)
        return long_lat_list
    
def insert_location_data(long_lat_list):
    conn, cursor = connect_database()
    cursor.executemany('''INSERT INTO postcodes VALUES (?,?,?)''', long_lat_list)
    conn.commit()
    conn.close()
       
def convert_postcodes():
    retrieved_postcodes = get_postcodes()
    api_data = api_convert(retrieved_postcodes)
    extracted_location_data = extract_long_lat(api_data)
    insert_location_data(extracted_location_data)
