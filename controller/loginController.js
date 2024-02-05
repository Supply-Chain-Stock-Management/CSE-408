function getLogin(req, res, next){
    //page render
    res.render("index", {
        title: "Login - SSCM",
    });
}

//do login
async function login(req, res, next){
    try{
        
    }
}

module.exports = {
    getLogin,
};