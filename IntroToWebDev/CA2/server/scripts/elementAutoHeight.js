'use strict';

class TextArea {
    constructor(element) {
        this.element = element
        this.clone = element.cloneNode(true)

        this.getLineHeight();
    }
    clearElement() {
        return new Promise(resolve => {
            this.element.value = 'BLEEP';
            this.element.style.height = '0px';
            this.element.style.padding = '0px';
            resolve(true)
        })
    }
    populateElement() {
        this.element.value = this.clone.value;
        this.element.style.height = this.scrollHeight + 'px';
        this.element.style.padding = this.clone.value;
    }
    async getLineHeight() {
        const _ = await this.clearElement()
        this.scrollHeight = this.element.scrollHeight;
        this.populateElement();
        return this.scrollHeight;
    }
    keyup() {
        let stringify = JSON.stringify(this.element.value)
        let length = [...stringify.matchAll(/\\n/gm)].length 
        this.element.style.height = this.scrollHeight * (length+1) + 'px'
    }
}

document.addEventListener('DOMContentLoaded', ()=> {
    const autoHeightArray = document.querySelectorAll('[autoheight]')
    autoHeightArray.forEach(element => {
        let textareaObject = new TextArea(element)
        textareaObject.element.addEventListener('keyup', ()=> {
            textareaObject.keyup();
        })
    })
})
