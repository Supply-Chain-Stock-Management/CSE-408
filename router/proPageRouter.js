//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getProduct} = require("../controller/proPageController");

const router = express.Router();

//get product info
router.get("/:id", getProduct);


module.exports = router;