const inventory = require("../models/inventoryFac");

async function getStock(req, res, next){
    try{
        console.log("poController")
        const inventories = await inventory.find();

        //page render
        res.render("purchaseOrder", {
            title: "Stock - SSCM",
            inventories: inventories,
        });
    }
    catch(err){
        next(err);
    }
}

async function dltOne(req, res, next){
    try{
        const row = await inventory.findByIdAndDelete({
            _id: req.params.id,
        });
    }
    catch(err){
        next(err);
    }
}

module.exports = {
    getStock,
    dltOne,
};