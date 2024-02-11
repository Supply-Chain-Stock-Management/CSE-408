const cart = require("../models/cart");
//getCart, addCart, dltCart, updateCart
async function getCart(req, res, next){
    try{
        console.log("cartController")
        const cart = await cart.find();

        //page render
        res.render("stock", {
            title: "Stock - SSCM",
            inventories: inventories,
        });
    }
    catch(err){
        next(err);
    }
}

module.exports = {
    getCart,
    //dltOne,
};
