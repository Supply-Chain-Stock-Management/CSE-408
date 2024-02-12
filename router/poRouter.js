//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getStock, dltOne, confirmed} = require("../controller/purchaseController");

const router = express.Router();

//show stock
router.get("/", getStock);

//dlt stock
router.delete("/:id", dltOne);

//post Confirm
router.post("/", confirmed);

module.exports = router;