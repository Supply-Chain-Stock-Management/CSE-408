const express = require('express');



// DB connection
const mongoose = require('mongoose');
const productRoutes = require('./routes/productRoutes');

// instantiate express
const app = express();

const PORT = 3000;
const MONGODB_URI = 'mongodb+srv://supply-chain.m9qvkts.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority';

const credentials = 'X509-cert-8379656237372897810.pem'
const options = {
  tlsCertificateKeyFile: credentials,
  serverApi: {
    version: '1', // Assuming ServerApiVersion.v1
  },
};
mongoose.connect(MONGODB_URI, options);



const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});
// DB connection




// Middleware to parse JSON requests
app.use(express.json());

// Use product routes
app.use('/products', productRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});