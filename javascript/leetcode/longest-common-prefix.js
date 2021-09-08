var longestCommonPrefix = function (strs) {
  const M = strs.length;
  if (M === 1) {
    return strs[0];
  }
  N = strs[0].length - 1;
  let answer = '';
  let idx = 0;
  while (idx <= N) {
    let candidate = strs[0][idx];
    for (let i = 1; i < M; i++) {
      if (strs[i].length - 1 < idx) {
        return answer;
      }
      if (strs[i][idx] !== candidate) {
        return answer;
      }
    }
    answer += candidate;
    idx += 1;
  }
  return answer;
};
