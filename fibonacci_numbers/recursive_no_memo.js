const getFib = (pos) => {
  if (pos == 0 || pos == 1) return pos;
  return getFib(pos - 1) + getFib(pos - 2);
};

console.log(getFib(1));
console.log(getFib(2));
console.log(getFib(3));
console.log(getFib(4));
console.log(getFib(5));
console.log(getFib(6));
