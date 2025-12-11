window.onload = () => {
  const elements = document.querySelectorAll(".random_color");
  elements.forEach((e) => {
    const red = Math.floor(Math.random() * 255);
    const blue = Math.floor(Math.random() * 255);
    const green = Math.floor(Math.random() * 255);

    const font_color = red + blue + green > 382 ? "black" : "white";
    //const anti_red = 255 - red;
    //const anti_blue = 255 - blue;
    //const anti_green = 255 - green;
    e.style.backgroundColor = `rgb(${red}, ${blue}, ${green})`;
    e.style.color = font_color;
  });
};
