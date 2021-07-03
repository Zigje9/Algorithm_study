function solution(s) {
  let firstFlag = true;
  let answer = '';
  for (let char of s) {
    if (char === ' ') {
      answer += char;
      firstFlag = true;
    } else {
      if (firstFlag) {
        answer += char.toUpperCase();
        firstFlag = false;
      } else {
        answer += char.toLowerCase();
      }
    }
  }
  return answer;
}
