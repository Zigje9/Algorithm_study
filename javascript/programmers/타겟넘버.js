function solution(numbers, target) {
  let answer = 0;
  const final = numbers.length;

  function dfs(nowIdx, value) {
    if (nowIdx === final) {
      if (value === target) {
        answer += 1;
      }
      return;
    }
    dfs(nowIdx + 1, value + numbers[nowIdx]);
    dfs(nowIdx + 1, value - numbers[nowIdx]);
  }
  dfs(0, 0);
  return answer;
}
