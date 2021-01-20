function solution(A) {
  const size = A.length
  const left = new Array(size).fill(0)
  const right = new Array(size).fill(0)
  if(size === 2){
      let max = A[0] > A[1] ? A[0] : A[1]
      return max = Math.max(max, A[0]+A[1])
  }

  left[0] = Math.max(0, A[0])
  for(let i=1 ; i<size ; i++){
      left[i] = Math.max(0, left[i-1]+A[i])
  }
  right[size-1] = Math.max(0, A[size-1])
  for(let i=size-2 ; i>=0 ; i--){
      right[i] = Math.max(0, right[i+1]+A[i])
  }
  let max = Math.max(A[0],A[size-1])
  for(let i=1 ; i<size-1 ; i++){
      max = Math.max(A[i]+left[i-1]+right[i+1], max)
  }
  return max
}
//부분합을 통해 왼쪽, 오른쪽 합배열 생성 합배열 -> 인덱스가 선택되었을때 최대값