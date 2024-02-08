const User = require("../models/people");
const createError = require("http-errors");

//import app.js
const app = require("../app");


function getLogin(req, res, next){
    //console.log("GetLogin func e dhuksi");
    //page render
    res.render("index", {
        title: "Login - SSCM",
    });
}

//do login
async function login(req, res, next){
    try{
        //find a user who has this username
        //console.log("Try e dhukse");
        const user = await User.findOne({
            name: req.body.username
        });
        if(user){
            //console.log("paise User");
            const result = req.body.password === user.location;
            if(result){
                //console.log("Rendering stock");
                res.render("dashboard", {
                    title: "Dashboard - SSCM",
                });
                // res.render("stock", {
                //     title: "Stock - SSCM",
                // });
                
            }
            else{
                throw createHttpError("Login failed!");
            }
        }
        else{
            //console.log("Ei 2nd error e dhukse");
            throw createError("Login failed!");
        }
    } catch(err){
        //console.log("Error khaitese");
        res.render("index", {
            errors: {
                common: {
                    msg: err.message,
                },
            },
        });
    }
};

module.exports = {
    getLogin,
    login,
};