function solution(A) { 
  let size = A.length
  if(size === 0){
      return 0
  }
  let min = A[0]
  let max = A[1]-A[0]
  for(let i=1 ; i<size ; i++){
      A[i] < min ? min = A[i] : min
      max = Math.max(max, A[i]-min)
  }
  return max
}
// min 값을 계속가지고 갱신