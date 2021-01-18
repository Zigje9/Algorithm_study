function solution(A) {
  const answer = [...new Set(A.sort((a, b) => a-b).filter(e => e>0))]
  if(answer.length === 0) return 1
  for (let i=0 ; i<answer.length ; i++){
      if (answer[i] != i+1){
          return i+1
      }
  }
  return answer[answer.length-1]+1
}
// 정수로 이루어진 배열에 포함되어있지 않은 양의 정수의 최소값