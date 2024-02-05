const mongoose = require('../index'); // Import your database connection
const Product = require('./Product');

const distributorSchema = new mongoose.Schema({
  name: { type: String, required: true },
  products: [Product.schema], // Embed Product schema in Distributor schema
});

const Distributor = mongoose.model('Distributor', distributorSchema);

module.exports = Distributor;
