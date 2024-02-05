//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getLogin} = require("../controller/loginController");

const router = express.Router();

//login page
router.get("/", getLogin);

module.exports = router;