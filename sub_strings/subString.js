/**
 *
 * @param {string} str
 */
const getSubString = (str) => {
  const res = [];
  for (let i = 0; i < str.length; i++)
    for (let j = i + 1; j <= str.length; j++) res.push(str.substring(i, j));

  return res;
};

console.log(getSubString('abc'));
