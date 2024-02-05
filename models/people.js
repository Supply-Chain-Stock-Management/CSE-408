const mongoose = require("mongoose");

const userSchema = mongoose.Schema(
    {
        entity_id: {
            type: Number,
            required: true,
        },
        type: {
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true,
        },
        location: {
            type: String,
            required: true,
        },
    },
    {
        timestamp: true,
    }
);
const people = mongoose.model("people", userSchema);
module.exports = people;