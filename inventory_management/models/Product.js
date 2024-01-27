const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  brand: { type: String },
  size: {type: String },
  category: { type: String },
  // Maximum Retail Price (MRP) is the highest price at which a product can be sold to the end consumer.
  mrp: { type: Number, default: 0 },
  description: { type: String },
});

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
