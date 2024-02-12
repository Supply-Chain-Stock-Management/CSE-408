const Cart = require("../models/cart");
const Product = require("../models/product");
const PoS = require("../models/POSchema");

//user id
const userId = 1;
//cart table
var myCart;
//all products of cart
var myAllProducts;


async function getStock(req, res, next){
    try{
        //console.log("poController")
        //get the cart by userId=CartId
        const cart = await Cart.find({cartID: userId});
        //console.log(cart);
        //get the product ids
        // var len = cart.products.length;
        // console.log(len);
        //fetch the product's info
        


        const prodsOfCart = cart[0].products;
        var allProducts = [];
        //console.log(prodsOfCart);
        for(var i = 0; i < prodsOfCart.length; i++){
            var prodId = prodsOfCart[i].productID;
            var product = await Product.find({ProductID: prodId});
            allProducts.push(product);
        }
        // console.log(allProducts);
        // console.log("Printing pro zerooooooo");
        // console.log(allProducts[0]);
        // console.log(allProducts[0][0].ProductID);
        // console.log(allProducts[1][0].ProductID);
        // //console.log(cart[0]);
        //console.log("All ok");
        //console.log("Render er aage");

        //storing for posting confirmed
        myCart = cart[0];
        myAllProducts = allProducts;

        //page render
        res.render("purchaseOrder", {
            title: "PO - SSCM",
            cart: cart[0],
            products: allProducts,
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

async function confirmed(req, res, next){
    //console.log("confirm  edhuksi")
    var prodArray=[];
var prodArrayWithFieldsNeeded=[];
    const cart = await Cart.find({cartID: userId});
    myCart = cart[0];
    const prodsOfCart = cart[0].products;
        var allProducts = [];
        //console.log(prodsOfCart);
        for(var i = 0; i < prodsOfCart.length; i++){
            var prodId = prodsOfCart[i].productID;
            var product = await Product.find({ProductID: prodId});
            allProducts.push(product);
        }
    myAllProducts = allProducts;
    for(var i=0; i< myAllProducts.length; i++){
        prodArray.push(myAllProducts[i][0]);
    }   

    //get the products with that fields
    if(myCart){
        for(var i = 0;i < prodArray.length; i++){
            var myProduct = {productID: prodArray[i].ProductID, MRP: prodArray[i].MRP, quantity: myCart.products[i].quantity};
            prodArrayWithFieldsNeeded.push(myProduct);
        }
    }


    //console.log("Array ta print");
    //console.log(prodArray);
    try{
        //console.log(myAllProducts);
        //myCart, myAllProducts,
        const data = new PoS({
            poID : 1001,
            source : "ARCS",
            products : prodArrayWithFieldsNeeded,
            createdOn : Date.now()
            }
        );
        const val = data.save();
        console.log(myCart);
                // Define the query to find the cart with cartID = 1
                const query = { cartID: 1 };
        
                // Define the update operation to clear the products array
                const update = { $set: { products: [] } };
                // Use findOneAndUpdate to find the cart with cartID = 1 and clear its products array
                await Cart.findOneAndUpdate(query, update);
        
                console.log('Products array cleared for cart with cartID = 1');
        
        
    }
    catch(err){
        next(err);
    }
}

module.exports = {
    getStock,
    dltOne,
    confirmed,
};