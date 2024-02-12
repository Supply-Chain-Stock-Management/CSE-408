//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getProduct, addToPO} = require("../controller/proPageController");

const router = express.Router();

//get product info
router.get("/:id", getProduct);

//process login
router.post("/:id", addToPO);


module.exports = router;