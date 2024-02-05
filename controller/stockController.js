function getStock(req, res, next){
    //page render
    res.render("stock", {
        title: "Stock - SSCM",
    });
}

module.exports = {
    getStock,
};