const mongoose = require("mongoose");

const productSchema = mongoose.Schema(
    {
        "ProductID": {
            type: Number,
            required: true,
        },
        "ProductName": {
            type: String,
            required: true,
        },
        "BrandName": {
            type: String,
            required: true,
        },
        "ProductSize": {
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