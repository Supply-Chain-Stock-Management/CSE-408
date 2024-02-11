const mongoose = require("mongoose");

const productSchema = mongoose.Schema(
    {
        "Product Name": {
            type: String,
            required: true,
        },
        "Brand Name": {
            type: String,
            required: true,
        },
        "Product Size": {
            type: String,
            required: true,
        },
        "Category": {
            type: String,
            required: true,
        },
        "MRP": {
            type: Number,
            required: true,
        },
        "Description": {
            type: String,
            required: true,
        },
    },
    {
        timestamp: true,
    }
);
const product = mongoose.model("product", productSchema);
module.exports = product;