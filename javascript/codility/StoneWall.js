function solution(H) {
  const stack = []
  let answer = 0
  for(let i=0 ; i<H.length ; i++){
      while(1){
          if(stack.length === 0){
              stack.push(H[i])
              break
          }
          if(stack[stack.length-1] === H[i]){
              break
          }
          if(stack[stack.length-1] > H[i]){
              stack.pop()
              answer += 1
              if(stack.length === 0){
                  stack.push(H[i])
                  break
              }
          }
          if(stack[stack.length-1] < H[i]){
              stack.push(H[i])
              break
          }
      }
  }
  return answer+stack.length
}