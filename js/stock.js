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

async function dltStock(invId){
    console.log("Dhukse re");
    let response = await fetch(`/inventories/${invId}`, {
      method: "DELETE",
    });
    let result = await response.json();

    if(result.errors){
      console.log("Error deleting");
    }
    else{
      document.getElementById(invId).remove();
    }
  }
  