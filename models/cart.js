const mongoose = require("mongoose");

const cartSchema = mongoose.Schema(
    {
        cartID: {
            type: Number,
            required: true,
        },
        products: [{
            productID: {
                type: Number,
                required: true,
            },
            MRP: {
                type: Number,
                required: true,
            },
            quantity: {
                type: Number,
                required: true,
                },
        }],

    },
    {
        timestamp: true,
    }
);
const cart = mongoose.model("cart", cartSchema);
module.exports = cart;