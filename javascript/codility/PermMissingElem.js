function solution(A) {
  A.sort((a, b) => a-b)
  let idx = 0
  while(1){
      if(A[idx] !== idx+1){
          break
      }
      idx++
  }
  return idx+1
}
// 1부터 정수로 나열된 배열에서 없는 값 찾기 