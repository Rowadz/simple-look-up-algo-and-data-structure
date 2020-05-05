const getFib = (pos) => {
  if (pos == 0 || pos === 1) return pos;
  let first = 0,
    second = 1,
    next = first + second;
  for (let i = 2; i < pos; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
};

console.log(getFib(1));
console.log(getFib(2));
console.log(getFib(3));
console.log(getFib(4));
console.log(getFib(5));
console.log(getFib(6));
