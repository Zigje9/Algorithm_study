function solution(A, B, K) {
  const big = parseInt(B/K)
  const small = parseInt((A-1)/K)
  if (A === 0){
      if (B === 0){
          return 1
      }
      return big + 1
  } 
  return big-small
}
// A, B 사이의 K의 배수의 개수 (0일때 예외처리)