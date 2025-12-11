"use strict";

window.onload = () => {
  // Colour h1 event
  const sign_up_text = document.getElementById("sign_up_text");
  const color_element = document.getElementById("color_input");
  if (color_element && sign_up_text) {
    color_element.addEventListener("input", () => {
      sign_up_text.style.color = color_element.value;
    });
  }

  // Age Selector Event
  const age_display = document.getElementById("age_display");
  const age_input = document.getElementById("age");
  if (age_input && age_display) {
    age_input.addEventListener("input", () => {
      age_display.innerHTML = age_input.value;
    });
  }

  // Submit Button Password Check
  const form_element = document.getElementById("form");
  const password_1 = document.getElementById("current_password");
  const password_2 = document.getElementById("password_confirm");
  if (form_element) {
    form_element.addEventListener("submit", (e) => {
      e.preventDefault();
      if (password_2.value !== password_1.value) {
        alert("Password Must Match!");
      }
    });
  }
};
