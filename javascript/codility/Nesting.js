function solution(S) {
  const answer = []
  for(let i=0 ; i<S.length ; i++){
      if(answer.length === 0){
          if(S[i] === ")"){
              return 0
          }
          answer.push(S[i])
      }
      else{
          if(answer[answer.length-1] === "("){
              if(S[i] === "("){
                  answer.push(S[i])
              }
              else{
                  answer.pop()
              }
          }
          else{
              return 0
          }
      }
  }
  return answer.length === 0 ? 1 : 0
}
// 괄호 스택