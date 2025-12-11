'use strict';

let currentWordCount = 0;
const wordSelectRegex = /\w+|\S+/g

document.addEventListener('DOMContentLoaded', ()=> {
    function initialize(){
        document.getElementById('good_things').addEventListener('keyup', (e)=> {
            checkWordCount(e, 1000)
        })
    }
    initialize()
})

const checkWordCount = (self, maxWordCount) => {
    let matches = [...self.target.value.matchAll(wordSelectRegex)]
    currentWordCount = matches.length
}
