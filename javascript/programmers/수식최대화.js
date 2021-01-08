const checkOperand = (atom) => {
  if (atom === '-' || atom === '+' || atom ==='*') return true
  return false
}

const makePriority = (priority) => {
  priority.push(["+","-","*"])
  priority.push(["+","*","-"])
  priority.push(["-","+","*"])
  priority.push(["-","*","+"])
  priority.push(["*","+","-"])
  priority.push(["*","-","+"])
}

const cal = (num1, num2, op) => {
  if (op === "+") return +num1 + +num2
  if (op === "-") return +num1 - +num2
  if (op === "*") return +num1 * +num2
}

const calculate = (operands, newEx) => {
  let expression = JSON.parse(JSON.stringify( newEx ))
  let value = 0
  for (let operand = 0 ; operand < 3 ; operand ++){
      let stack = []
      let result = 0
      while(true){
          if(expression.length === 0){
              expression = stack
              break
          }
          if(expression[0] === operands[operand]){
              result = cal(stack[stack.length-1],expression[1],expression[0])
              stack.pop()
              stack.push(result)
              expression.shift()
              expression.shift()
          }
          else{
              stack.push(expression[0])
              expression.shift()
          }
      }
  }
  return Math.abs(expression[0])
}

const solution = (expression) => {
  const atoms = expression.split("")
  const operands = []
  atoms.map((val, idx) => checkOperand(val) ? operands.push([val,idx]) : true)
  const newEx = []
  let tempStr = ""
  let j = 0;
  for(let i = 0 ; i < atoms.length ; i++){
      if(j<operands.length){
          if(i === operands[j][1]){
          newEx.push(tempStr)
          newEx.push(operands[j][0])
          j+=1
          tempStr=""
          }
          else{
            tempStr += atoms[i]   
          }
      }
      else{
        tempStr += atoms[i]   
      }
  }
  newEx.push(tempStr)
  const priority = []
  makePriority(priority)
  let answer = 0 
  for (let pri of priority) {
      let value = calculate(pri, newEx)
      value > answer ? answer = value : answer
  }
  return answer
}
//  💩 코드 반성..