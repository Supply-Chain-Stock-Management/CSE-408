const mongoose = require("mongoose");

const inventorySchema = mongoose.Schema(
    {
        quantity: {
            type: Number,
            required: true,
        },
        unrestricted: {
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