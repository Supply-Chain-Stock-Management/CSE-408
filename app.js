const express = require("express");
const dotenv = require("dotenv");
const mongoose = require("mongoose");
const path = require("path");
const cookieParser = require("cookie-parser");
const loginRouter = require("./router/loginRouter");
const stockRouter = require("./router/stockRouter");


//internal import
const {notFoundHandler, errorHandler} = require("./middleware/errorHandler");

const app = express();
dotenv.config();

//database conn
mongoose.connect(process.env.MONGO_CONN_STRING, {
}).then(() => console.log("database connection successful!"))
.catch(err => console.log(err));

//req parser
app.use(express.json());
app.use(express.urlencoded({extended: true}));

//set view engine
app.set("view engine", "ejs");

//set static folder
app.use(express.static(path.join(__dirname, "public")));

//parse cookie
app.use(cookieParser(process.env.COOKIE_SECRET));


//routing setup
app.use('/', loginRouter);
//login kore apatoto stock e jabe
app.use('/stock', stockRouter);


//error handling

//not found
app.use(notFoundHandler);

//default error handler
app.use(errorHandler);


app.listen(process.env.PORT, ()=>{
    console.log(`Listening to port ${process.env.PORT}`);
});