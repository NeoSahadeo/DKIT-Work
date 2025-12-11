'use strict';


class Popcorn {
    constructor(element) {
        this.element = element;
        this.currentPopOverState = false;

        this.onMouseEnter()
        this.onMouseExit()

        this.popOverContainer = document.createElement('span')
    }

    startTimer() {
        this.timer = setTimeout(()=>{
            this.createPopOver()
        }, 0) 
    }
    cancelTimer() {
        if(this.timer) {
            clearTimeout(this.timer)
        }
    }
    onMouseEnter() {
        this.element.addEventListener('mouseenter', ()=> {
            this.startTimer()
        })
    }
    onMouseExit() {
        this.element.addEventListener('mouseleave', ()=> {
            this.cancelTimer()
            this.deletePopOver()
        })
    }
    createPopOver() {
        this.popOverContainer.innerHTML = this.element.popcorn 
    }
    deletePopOver() {
    }
}
document.addEventListener('DOMContentLoaded', ()=>{
    let kernels = document.querySelectorAll('[popcorn]')
    kernels.forEach(element => {
        startTimer(element)
    })
})
function startTimer(element){
    let popcornObject = new Popcorn(element)
}
