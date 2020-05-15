/**
 * @param {string} str
 */
const isPalindrome1 = (str) => {
  const reverseStr = str.split('').reverse().join('');
  return reverseStr === str;
};

console.log(isPalindrome1('aaa'));
console.log(isPalindrome1('abc'));

/**
 * @param {string} str
 */
const isPalindrome2 = (str) => {
  for (let i = 0; i < str.length / 2; i++)
    if (str[i] !== str[str.length - 1 - i]) return false;
  return true;
};

console.log(isPalindrome2('aaa'));
console.log(isPalindrome2('abc'));
