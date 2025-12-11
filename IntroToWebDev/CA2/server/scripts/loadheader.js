'use strict';

document.addEventListener('DOMContentLoaded', function(){
    const xhttp = new XMLHttpRequest() 

    // Scan for meta page tag and add a load event
    const metaPage = document.querySelector('meta[name="page"]').content
    xhttp.addEventListener('load', xhttpListener)

    // switch folders heirarchy
    if (metaPage == 'home'){
        xhttp.open("GET", "./partials/header.html")
    }else{
        xhttp.open("GET", '../partials/header.html')
    }
    xhttp.send()

    function xhttpListener(){
        // Push header content into the header
        const header = document.getElementsByTagName('header')[0]
        header ? header.insertAdjacentHTML("afterbegin", this.response) : undefined;

        // scan for 'navlinks' 
        const navLinks = document.querySelectorAll('#desktopNav > ul > li > a')
        const nav = document.querySelector('#desktopNav')

        // Calculate the relative 'href' links for index.html
        const metaPage = document.querySelector('meta[name="page"]').content
        if (metaPage == 'home'){
            const regexSelectorEnd = /(\/.*){2}/g
            const regexSelectorBase = /^.*(?=\/)/g
            // document.querySelector('#logoLink').href = "./"
            navLinks.forEach(element =>{
                if (element.id != 'home'){
                    let matches = [...element.href.matchAll(regexSelectorEnd)]
                    let baseMatches = [...element.href.matchAll(regexSelectorBase)]
                    matches.forEach((matched, index) => {
                        element.href = baseMatches[0]+'/pages'+matched[1]
                    })
                } else{
                    element.href = './'
                }
            })
        }
    }
})
