function solution(A) {
  const left = new Array(A.length).fill(0)
  const right = new Array(A.length).fill(0)
  let temp
  for(let i=1 ; i<A.length-1 ; i++){
      temp = left[i-1] + A[i]
      left[i] = temp > 0 ? temp : 0
  }
  for(let i=A.length-2 ; i>0 ; i--){
      temp = right[i+1] + A[i]
      right[i] = temp > 0 ? temp : 0
  }
  let max = 0
  for(let i=1 ; i<A.length-1 ; i++){
      max < left[i-1]+right[i+1] ? max = left[i-1]+right[i+1] : max
  }
  return max
}
//부분합 이용하기 