const mongoose = require("mongoose");

const poSchema = mongoose.Schema(
    {
        poID: {
            type: Number,
            required: true,
        },
        source: {
            type: String,
            required: true,
        },
        createdOn: {
            type: Date,
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
const poS = mongoose.model("poS", poSchema);
module.exports = poS;