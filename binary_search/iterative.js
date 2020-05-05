const binarySearch = (arr, el) => {
  let low = 0,
    heigh = arr.length;
  while (low < heigh) {
    const mid = Math.floor((low + heigh) / 2);
    if (arr[mid] === el) return true;
    if (arr[mid] > el) heigh = mid - 1;
    else low = mid + 1;
  }
  return false;
};

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(binarySearch(arr, 10));
console.log(binarySearch(arr, 1));
console.log(binarySearch(arr, -1));
console.log(binarySearch(arr, 3232));
