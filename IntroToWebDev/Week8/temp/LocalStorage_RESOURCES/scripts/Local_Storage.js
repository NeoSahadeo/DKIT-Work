'use strict';

let nameElement
let timer

document.addEventListener('DOMContentLoaded', initialization);

function initialization(){
    nameElement = document.querySelector('#theName') ? document.querySelector('#theName') : null;
    if (nameElement){
        nameElement.addEventListener('keyup', nameLengthHandler)
        nameElement.addEventListener('keydown', ()=>{clearCurrentTimeout(timer)})
    }
}

async function nameLengthHandler(){
    if (nameElement.value.length < 3){
        let timerDestroyed = await clearCurrentTimeout(timer)
        if (timerDestroyed){
            timer = setTimeout(()=>{
                document.getElementById('nameLengthIndicator').classList.remove('hidden');
                document.getElementById('submitForm').setAttribute('disabled', true)
            }, 500)
        }
    }else{
        clearCurrentTimeout(timer)
        document.getElementById('nameLengthIndicator').classList.add('hidden');
        document.getElementById('submitForm').removeAttribute('disabled', true)
    }
}
const clearCurrentTimeout = (timerName) => {
    if (timerName){
        clearTimeout(timerName)
    }
    return true
}

// This should be a list of all items needed to be stored (the 'id names')
// and the id in storage
// ['id in html', 'id in storage']
const storeME = [
    ['theName', 'the_name'],
    ['theAge', 'the_age'],
    ['theCountry', 'the_country'],
    ['theEmail', 'the_email'],
    ['favouriteDay', 'favourite_day'],
    ['favouriteColour', 'favourite_colour'],
    ['favouriteDay', 'favourite_day'],
    ['vanilla', 'vanilla'],
]
function checkForm() {
    if (document.getElementById('theName').value.length < 3) {
        alert("The name is not long enough: 3 or more characters please.") 
        document.getElementById('theName').select()
        return false;
    }

    storeME.forEach(element => {
        if (document.getElementById(element[0])) {
            localStorage.setItem(element[1],document.getElementById(element[0]).value)
        }
    })
    return true;
}


function readLocalStorage(){
    storeME.forEach(element => {
        if (document.getElementById(element[0])){
            document.getElementById(element[0]).innerText = localStorage.getItem(element[1]) 
        }
    })
}
