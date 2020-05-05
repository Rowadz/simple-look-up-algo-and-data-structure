const bubbleSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
};

console.log(bubbleSort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]));
console.log(bubbleSort([21, 4, 1, 3, 9, 20, 25, 6, 1, -1]));
