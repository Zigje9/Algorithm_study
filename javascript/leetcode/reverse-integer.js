var reverse = function (x) {
  let minus = false;
  if (x < 0) {
    minus = true;
  }

  function getResult(arr) {
    return arr.reduce((acc, cur, index) => {
      return acc + cur * 10 ** index;
    }, 0);
  }
  let answer = 0;
  minus ? (answer = getResult(x.toString().split('').slice(1)) * -1) : (answer = getResult(x.toString().split('')));
  if (answer > 2 ** 31 - 1) {
    return 0;
  }
  if (answer < 2 ** 31 * -1) {
    return 0;
  }
  return answer;
};
