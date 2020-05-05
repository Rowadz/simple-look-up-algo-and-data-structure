const binarySearch = (arr, el, low, heigh) => {
  if (low >= heigh) return false;
  const mid = Math.floor((low + heigh) / 2);
  if (arr[mid] === el) return true;
  if (arr[mid] > el) return binarySearch(arr, el, low, mid - 1);
  else return binarySearch(arr, el, mid + 1, heigh);
};

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(binarySearch(arr, 10, 0, arr.length));
console.log(binarySearch(arr, 1, 0, arr.length));
console.log(binarySearch(arr, -1, 0, arr.length));
console.log(binarySearch(arr, 3232, 0, arr.length));
