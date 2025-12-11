'use strict';

document.addEventListener('DOMContentLoaded', function(){
    const xhttp = new XMLHttpRequest() 

    // Scan for meta page tag and add a load event
    const metaPage = document.querySelector('meta[name="page"]').content
    xhttp.addEventListener('load', xhttpListener)

    // switch folders heirarchy
    if (metaPage == 'home'){
        xhttp.open("GET", "./partials/footer.html")
    }else{
        xhttp.open("GET", '../partials/footer.html')
    }

    xhttp.send()
    function xhttpListener() {
        const footer = document.getElementsByTagName('footer')[0]
        footer ? footer.insertAdjacentHTML('afterbegin', this.response) : undefined;
    }
})

