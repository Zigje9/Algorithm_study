function solution(A) {
  const permutation = A.sort((a, b) => a-b)
  for(let i=0 ; i<permutation.length ; i++){
      if(permutation[i] !== i+1){
          return 0
      }
  }
  return 1
}
// 1부터 이루어지는 순열인지 체크 