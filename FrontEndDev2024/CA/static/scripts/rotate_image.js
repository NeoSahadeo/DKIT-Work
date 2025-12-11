"use strict";

window.onload = () => {
  const element = document.querySelector('[alt="Baby Panda"]');
  if (element) {
    element.addEventListener("contextmenu", (e) => {
      e.preventDefault();
      let current_rotation = parseInt(element.style.rotate);
      if (isNaN(current_rotation)) {
        current_rotation = 0;
      }
      element.style.rotate = `${45 + current_rotation}deg`;
    });
  }
};
