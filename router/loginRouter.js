//external imports
const express = require("express");
const dotenv = require("dotenv");

const {getLogin, login} = require("../controller/loginController");

const router = express.Router();

//login page
router.get("/", getLogin);

//process login
router.post("/", login);

module.exports = router;