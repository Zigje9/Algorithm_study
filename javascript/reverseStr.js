function solution(data) {
  let answer = '';
  for (let c of data) {
    answer = c + answer;
  }
  return answer;
}
