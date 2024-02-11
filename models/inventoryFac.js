const mongoose = require("mongoose");

const inventorySchema = mongoose.Schema(
    {
        productID: {
            type: Number,
            required: true,
        },
        productName: {
            type: String,
            required: true,
        },
        quantity: {
            type: Number,
            required: true,
        },
        inQC: {
            type: Number,
            required: true,
        },
        inTransit: {
            type: Number,
            required: true,
        },
    },
    {
        timestamp: true,
    }
);
const inventory = mongoose.model("inventory", inventorySchema);
module.exports = inventory;