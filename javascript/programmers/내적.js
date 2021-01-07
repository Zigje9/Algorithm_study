function solution(a, b) {
  let answer = 0
  for(let i=0 ; i < a.length ; i++){
      answer += a[i]*b[i]
  }
  return answer;
}
// return a.reduce((acc, cur, idx) => acc += cur*b[idx], 0)
// reduce 함수로 한번에 가능