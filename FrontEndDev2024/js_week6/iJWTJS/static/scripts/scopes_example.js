const x = 0;
console.log(x);

(() => {
  console.log(x);
})();

//(() => {
//  const y = 0;
//})();
//
//console.log(y);

(() => {
  window.y = 1;
})();
console.log(window.y);
