const change = (char) => {
  switch (char) {
      case "}":
          return "{"
          break
      case "]":
          return "["
          break
      case ")":
          return "("
          break    
  }
}

function solution(S) {
  const stack = []
  S.split("").map((e) => {
      if(stack.length === 0){
          stack.push(e)
      }
      else{
          if(stack[stack.length-1] === change(e)){
              stack.pop()
          }
          else{
              stack.push(e)
          }
      }
  })
  return stack.length === 0 ? 1 : 0
}
// stack 에 추가하고 제거하기 