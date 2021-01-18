// 0과1의 배열 A<B 를 만족하는 0,1 순서쌍의 개수 
function solution(A) {
  let total = A.reduce((acc, cur) => acc+cur)
  let answer = 0
  for (let i=0 ; i<A.length ; i++){
      if(answer>1000000000) return -1
      if(A[i]===0){
          answer += total
      }
      else{
          total -= 1
      }
  }
  return answer
}