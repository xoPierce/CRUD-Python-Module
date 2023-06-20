#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:00:21 2023

@author: jefferywaren_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'hardpassword'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32480
        DB = 'AAC1'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection Successful")


    # A Create method that inserts a document into a specified MongoDB database and collection
    def create(self, data):
        try:
            # Checks if the data parameter is empty
            if data is not None:
                self.database.animals.insert_one(data)  # data should be dictionary
                # Returns true if the document is created/inserted successfuly
                return True      
            # If the data parameter is empty, return False
            elif data is None:
                    return False
        except:
            raise Exception ("Data parameter is incorrectly formatted")
            
            
    # A Read method that queries for document(s) from a specified MongoDB database and specified collection
    def read(self, data):
        # Creates an empty list to add all of the search results to
        result = []
        try:
            # Checks if the data parameter is empty
            if data is not None:
                # Adds all of the returned searches in to the result list
                result = self.database.animals.find(data)  # data should be dictionary
                return result 
            # Returns an empty list of the data parameter is empty
            elif data is None:
                return result
        except:
            raise Exception ("Data parameter is incorrectly formatted")


    # An Update method that queries for and changes document(s) from a specified MongoDB database and specified collection
    def update(self, data_to_change, new_data):
        try:
            # Checks if both of the data parameters are empty
            if data_to_change is not None or new_data is not None:
                updated = self.database.animals.update_many(data_to_change, new_data)
                # Returns the cursor object 
                return updated
            # If the data parameter is empty, raise exception
            elif data_to_change is None or new_data is None:
                # Returns 0 if there is no data
                return 0
        except:
            raise Exception ("Data parameter is incorrectly formatted")
            
            
    # A Delete method that queries for and removes document(s) from a specified MongoDB database and specified collection       
    def delete(self, data_to_delete):
        try:
            # Checks if the data parameter is empty
            if data_to_delete is not None:
                deleted = self.database.animals.delete_many(data_to_delete)
                return deleted
            # If the data parameter is empty, raise exception
            else:
                # raise Exception("Nothing to read, because data_to_delete parameter is empty")
                return 0
        except:
            raise Exception ("Data parameter is incorrectly formatted")
        
        