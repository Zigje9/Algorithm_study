var romanToInt = function (s) {
  const Roman = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const N = s.length - 1;
  let nowIdx = 0;
  let answer = 0;
  const numArr = s.split('');
  while (nowIdx <= N) {
    if (nowIdx === N) {
      answer += Roman[numArr[nowIdx]];
      break;
    }
    if (Roman[numArr[nowIdx]] < Roman[numArr[nowIdx + 1]]) {
      answer += Roman[numArr[nowIdx + 1]] - Roman[numArr[nowIdx]];
      nowIdx += 2;
    } else {
      answer += Roman[numArr[nowIdx]];
      nowIdx += 1;
    }
  }
  return answer;
};
