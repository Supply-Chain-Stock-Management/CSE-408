//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getStock} = require("../controller/stockController");

const router = express.Router();

//login page
router.get("/stock", getStock);

module.exports = router;