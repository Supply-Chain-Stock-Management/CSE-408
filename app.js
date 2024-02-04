//import css  from './css/stock.css';
    

const express = require('express')
const {connectToDb,getDb} = require('./db', 'db.secondary')
const path = require('path')
const mongoose = require('mongoose')
//init app
const app = express()
app.use(express.static(path.join(__dirname,'public')))

// set the view engine to ejs
app.set('view engine', 'ejs');

const productSchema = new mongoose.Schema({
    _id : Number,
    productName : String,
    quantity : Number,
    unrestricted : Number,
    inTransit : Number
});


// use res.render to load up an ejs view file

// index page
app.get('/', function(req, res) {
  res.render('pages/index');
});

// about page
app.get('/about', function(req, res) {
  res.render('pages/about');
});


// db connection
let db 
connectToDb((err) => {
    if (!err) {
        app.listen(3000,()=>{
            console.log('app listening on port 3000')
        })
        db = getDb()
    }
})

//convert collection to array
app.get('/inventory',(req,res)=>{
    let products = []
     db.collection('factoryInventory').find()
     .forEach(product =>products.push(product))
        .then(()=> {
            //res.status(200).json(products)
            res.render('pages/inventory', {products: products});
        })
        .catch(()=>{
            res.status(500).json({error:"Couldn't fetch products"})
        })
})

//convert collection to array
app.get('/users',(req,res)=>{
    let users = []
     db.collection('factoryInventory').find()
     .forEach(product =>products.push(product))
        .then(()=> {
            res.status(200).json(products)
        })
        .catch(()=>{
            res.status(500).json({error:"Couldn't fetch products"})
        })
})

//routes
app.get('/products',(req,res)=>{
    let products = []
    db.collection('products').find()
     .forEach(product =>products.push(product))
        .then(()=> {
            res.status(200).json(products)
        })
        .catch(()=>{
            res.status(500).json({error:"Couldn't fetch products"})
        })
})
//assuming app is express Object.
app.get('/stock',function(req,res) {
    res.sendFile(path.join(__dirname+'/stock.html'));
});

const addQuery = (req, res, next) => {
    req.url = req.url + `?id=someID&p=bag`;
    next();
}
//create an api that takes a query parameter and returns the products that match the query
app.get('/products/:category',(req,res)=>{
    let products = []
     db.collection('products').find({"Category":req.params.category})
     .forEach(product =>products.push(product))
        .then(()=> {
            res.status(200).json(products)
        })
        .catch(()=>{
            res.status(500).json({error:"Couldn't fetch products"})
        })
})

app.get('/p?tagId=/', function(request, response) {
    // userId is a parameter in the url request
    response.writeHead(200); // return 200 HTTP OK status
    response.end('You are looking for tagId' + request.route.query.tagId);
  })

app.get('/stock/sort', (req,res)=>{
    var query = "Brand Name"
    let products = []
    var mySort = { "Brand Name": 1 };
     db.collection('products').find()
     .sort(mySort)
     .forEach(product =>products.push(product))
        .then(()=> {
            res.status(200).json(products)
        })
        .catch(()=>{
            res.status(500).json({error:"Couldn't fetch products"})
        })
})
