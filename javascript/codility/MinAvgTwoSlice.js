// 2개이상 slice하여 평균의 최솟값
// 구글링해서 평균의 최솟값은 2개 혹은 3개에서 나오는 힌트로 풀이
function solution(A) {
  const size = A.length
  let min = 10000
  let index = 100000
  for (let i=0 ; i<=size-2 ; i++){
      if((A[i]+A[i+1])/2 < min){
          min = (A[i]+A[i+1])/2
          index = i
      }
  }
  for (let i=0 ; i<=size-3 ; i++){
      if((A[i]+A[i+1]+A[i+2])/3 < min){
          min = (A[i]+A[i+1]+A[i+2])/3
          index = i
      }
      if((A[i]+A[i+1]+A[i+2])/3 === min){
          if(index>i){
              index = i
          }
      }
  }
  return index
}