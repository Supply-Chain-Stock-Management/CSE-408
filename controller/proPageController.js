const product = require("../models/product");

let productId;
async function getProduct(req, res, next){
    try{
        console.log("proPageController e dhukse")
        //const productt = await product.find({"Product ID": req.params.id});
        
        productId = req.params.id;
        console.log(productId)
        const aProduct = await product.findOne({ProductID: productId});
        
        //console.log(aProduct);
        //page render
        res.render("productPage", {
            title: "Product - SSCM",
            aProduct: aProduct,
        });
    }
    catch(err){
        next(err);
    }
}


module.exports = {
    getProduct,
};