//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getCart/*, addCart, dltCart, updateCart*/} = require("../controller/cartController");

const router = express.Router();

//get cart
router.get("/", getCart);
/*
//add to cart
router.post("/", addCart);

//dlt from cart
router.delete("/:id", dltCart);

//update cart
router.put("/:id", updateCart);
*/
module.exports = router;