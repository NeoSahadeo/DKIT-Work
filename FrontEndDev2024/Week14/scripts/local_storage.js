function password_checker(password) {
  if (password.length > 4) {
    return true;
  }

  alert("Password is too short.");
  return false;
}

function cache_control({ method, name, data } = {}) {
  if (method === "set") window.localStorage.setItem(`peter_${name}`, data);
  if (method === "delete") window.localStorage.removeItem(`peter_${name}`);
  if (method === "clear") window.localStorage.clear();
  if (method === "get") {
    const data = window.localStorage.getItem(`peter_${name}`);
    return data ? data : undefined;
  }
}
