from pymongo import MongoClient

credentials = 'X509-cert-8379656237372897810.pem'
uri = "mongodb+srv://supply-chain.m9qvkts.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=credentials)

db = client['testDB']
collection = db['testCol']
doc_count = collection.count_documents({})
print(doc_count)
