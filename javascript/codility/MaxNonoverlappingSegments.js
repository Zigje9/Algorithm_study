function solution(A, B) {
  if(A.length === 0){
      return 0
  }
  if(A.length === 1){
      return 1
  }

  let answer = 1
  let end = B[0]
  const N = A.length 
  for(let i=1 ; i<N ; i++){
      if(A[i] > end){
          answer += 1
          end = B[i]
      }
  }
  return answer
}