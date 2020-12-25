#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the MongoClient class
from pymongo import MongoClient, errors
import json
import smtplib
import os
from email.message import EmailMessage

def mail(access_denied):

    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)

    msg = EmailMessage()
    msg.set_content('ALERT! Nginx access has been denied more than 10 times. Please have a look at the server')
    msg['Subject'] = 'ALERT! Access Denied - Nginx'
    msg['From'] = "vigneshkarthy3@gmail.com"
    msg['To'] = "vigneshkarthy3@gmail.com"
    mailServer.starttls()
    mailServer.login("vigneshkarthy3@gmail.com","pass")
    mailServer.send_message(msg)
    mailServer.quit()

    return access_denied

# use a try-except indentation to catch MongoClient() errors
if __name__ == "__main__":

    try:
        # global variables for MongoDB host (default port is 27017)
        DOMAIN = 'mongodb'
        PORT = 27017
        my_path = "/usr/src/app/access_nginx.log"
        # try to instantiate a client instance
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = "root",
            password = "root",
        )

        # print the version of MongoDB server if connection successful
        # print ("server version:", client.server_info()["version"])

        # get the database_names from the MongoClient()
        database_names = client.list_database_names()
        db=client.database
        db.access.drop()
        collection=db.access

        if os.path.exists(my_path) and os.path.getsize(my_path) > 0:

            with open(my_path) as filecontent:
                for i in filecontent:
                    content_dict=json.loads(i)
                    collection.insert_one(content_dict)

            failed_attempt= collection.find({"status": "401"}).count()
            if failed_attempt > 10:
                mail(failed_attempt)
        else:
            print("File is empty and non-existent")


        # Printing the data inserted
        # cursor = collection.find()
        # for record in cursor:
        #     print(record)
        # collection_names = db.collection_names(include_system_collections=False)

    except errors.ServerSelectionTimeoutError as err:
        # set the client and DB name list to 'None' and `[]` if exception
        client = None
        # catch pymongo.errors.ServerSelectionTimeoutError
        print ("pymongo ERROR:", err)
