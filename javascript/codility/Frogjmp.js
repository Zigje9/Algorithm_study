function solution(X, Y, D) {
  let answer = Math.floor((Y-X)/D)
  if((Y-X)%D === 0) return answer
  return answer+1
}
//parseInt 사용시 big int 처리불가로 에러 발생 하여 Math.floor 로 변경 (정수값으로 내림)