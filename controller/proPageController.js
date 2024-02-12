const product = require("../models/product");
const inventory = require("../models/inventoryFac");
const cart = require("../models/cart");

let productId, mrp;
async function getProduct(req, res, next){
    try{
        //console.log("proPageController e dhukse")
        //const productt = await product.find({"Product ID": req.params.id});
        
        productId = req.params.id;
        //console.log(productId)
        const aProduct = await product.findOne({ProductID: productId});
        const productFromInv = await inventory.findOne({productID: productId});
        
        //MRP for PO
        mrp = aProduct.MRP;

        //console.log(aProduct);
        //page render
        res.render("productPage", {
            title: "Product - SSCM",
            aProduct: aProduct,
            productFromInv: productFromInv,
        });
    }
    catch(err){
        next(err);
    }
}

//do login
async function addToPO(req, res, next){
    try{
        //console.log("Dhuksi");
        const quantity = req.body.quantity;
        //console.log(quantity);
        // let newCart;
        // newCart = new cart({
        //     cartID: 1,
        //     person.friends.push(friend);
        //     person.save(done);
        // });
        var currProduct = {productID: productId, MRP: mrp, quantity: quantity};
        //console.log("product thikk");
        // cart.cartID = 1;

        // cart.update(
        //     { cartID: 1 }, 
        //     { $addToSet: { products: currProduct } }
        //   );
        
        const aCart = await cart.findOne({cartID: 1});
        //console.log("Acart paisi");
        if(aCart.products.length >= 0){
            //update
            // console.log("if er moddhe");
            // console.log(productId);
            var currProd = {productID: productId, MRP: mrp, quantity: quantity};
            aCart.products.push(currProd);
            // console.log("push");
            // console.log(aCart);
            //            const val = cart.save();
            await aCart.save();
            //console.log("Updated");
        }
        else{
            var currProd = {productID: productId, MRP: mrp, quantity: quantity};
            const data = new cart({
                cartID: 1,
                products: currProd
            });
            const val = data.save();
            //console.log("Updated");
        }
        
        
    }
    catch(err){
        next(err);
    }

};

module.exports = {
    getProduct,
    addToPO,
};