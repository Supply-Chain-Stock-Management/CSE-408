function addProShow() {  
    var cardPart = document.getElementById('addCard');
    cardPart.style.cssText += 'visibility: visible';
    var mainPage = document.getElementById('mainPage');
    mainPage.style.cssText += 'opacity: 0.3';
}  

function resetNow(){
    var cardPart = document.getElementById('addCard');
    cardPart.style.cssText += 'visibility: hidden';
    var mainPage = document.getElementById('mainPage');
    mainPage.style.cssText += 'opacity: 1';
}