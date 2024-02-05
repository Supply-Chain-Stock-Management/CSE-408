import pandas as pd
from pymongo import MongoClient

def populate(excel, sheet_name, collection_name):
    # Connect to MongoDB Atlas
    credentials = 'X509-cert-8379656237372897810.pem'
    uri = "mongodb+srv://supply-chain.m9qvkts.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    project = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=credentials)
    
    
    db = project['inventory']

    # Read data from Excel file
    collection = db[collection_name]
    documnets = pd.read_excel(excel, sheet_name)
    # Convert data to JSON format
    documnets = documnets.to_dict('records')

    # Insert data into MongoDB collections
    collection.insert_many(documnets)

    # Close the MongoDB connection
    project.close()

