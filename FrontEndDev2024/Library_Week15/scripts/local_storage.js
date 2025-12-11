function save_data() {
  const username = document.getElementById("username");
  const password = document.getElementById("password");
  const age = document.getElementById("age");
  const location = document.getElementById("location");

  localStorage.setItem("username", username.value);
  localStorage.setItem("password", password.value);
  localStorage.setItem("age", age.value);
  localStorage.setItem("location", location.value);
}

function get_data() {
  const username = localStorage.getItem("username");
  const password = localStorage.getItem("password");
  const age = localStorage.getItem("age");
  const location = localStorage.getItem("location");

  const username_element = document.getElementById("username");
  const password_element = document.getElementById("password");
  const age_element = document.getElementById("age");
  const location_element = document.getElementById("location");

  console.log(username);

  username_element.innerHTML = username;
  password_element.innerHTML = password;
  age_element.innerHTML = age;
  location_element.innerHTML = location;
}
