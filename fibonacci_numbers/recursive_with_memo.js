const feb = n => {
  const countingFunc = (remaning, saved) => {
    if (remaning == 0 || remaning == 1) return remaning;
    if (remaning in saved) return saved[remaning];
    saved[remaning] = countingFunc(remaning - 1, saved) + countingFunc(remaning - 2, saved);
    return saved[remaning];
  };
  return countingFunc(n, {});
};
