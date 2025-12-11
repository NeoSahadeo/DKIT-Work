async function load_header() {
  try {
    const response = await fetch(`http://localhost:8000/partials/header.html`);
    if (response.ok) {
      document.body
        .querySelector("header")
        .insertAdjacentHTML("afterbegin", await response.text());
      return 0;
    }
  } catch (error) {
    console.error("Error in header loading", error);
    return 1;
  }
}

load_header();
