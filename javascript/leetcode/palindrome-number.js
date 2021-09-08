var isPalindrome = function (x) {
  if (x < 0) {
    return false;
  }
  const numArr = x.toString().split('');
  const N = numArr.length - 1;
  for (let i = 0; i <= Math.floor(N / 2); i++) {
    if (numArr[i] !== numArr[N - i]) {
      return false;
    }
  }
  return true;
};
