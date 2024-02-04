const MongoClient = require('mongodb').MongoClient;

let dbConnection
let uri = 'mongodb+srv://walkersarf:cr7tk8kb9@supply-chain.6oxukxh.mongodb.net/?retryWrites=true&w=majority'
module.exports = {
    connectToDb: (cb) => {
        MongoClient.connect(uri)
            .then((client) => {
                dbConnection = client.db('central')
                console.log("Successful Connection")
                return cb()
            })
            .catch(err => {
                console.log(err)
                return cb(err)
            })
    },
    getDb: () => dbConnection
} 
