const mongoose = require('../index'); // Import your database connection
const Product = require('./Product');

const factorySchema = new mongoose.Schema({
  name: { type: String, required: true },
  products: [Product.schema], // Embed Product schema in Factory schema
});

const Factory = mongoose.model('Factory', factorySchema);

module.exports = Factory;
