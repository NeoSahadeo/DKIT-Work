import { iJWT } from "./ijwt.js";
const ijwt = new iJWT({ mode: "development" });

const image_element = document.createElement("div");
const image_element_style = image_element.style;

image_element_style.backgroundImage = `url(${ijwt.url_string_resolver("/static/images/starry_boat.jpg")})`;
image_element_style.width = "100%";
image_element_style.paddingTop = "100%";
image_element_style.backgroundPosition = "center";
image_element_style.backgroundSize = "cover";

document.getElementById("image_example_1")?.appendChild(image_element);

const image_tag = document.createElement("img");
image_tag.src = ijwt.url_string_resolver("/static/images/starry_boat.jpg");
image_tag.alt = "Starry Boat";
image_tag.style.width = "100%";

document.getElementById("image_example_2")?.appendChild(image_tag);
