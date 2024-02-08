//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getStock, dltOne} = require("../controller/stockController");

const router = express.Router();

//show stock
router.get("/", getStock);

//dlt stock
router.delete("/:id", dltOne);

module.exports = router;