const mongoose = require('../index'); // Import your database connection
const Product = require('./Product');

const warehouseSchema = new mongoose.Schema({
  name: { type: String, required: true },
  products: [Product.schema], // Embed Product schema in Warehouse schema
});

const Warehouse = mongoose.model('Warehouse', warehouseSchema);

module.exports = Warehouse;
