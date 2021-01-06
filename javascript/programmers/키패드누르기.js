const makeKeypad = (keypad) => {
  let a,b
  for(let i=1 ; i<10 ; i++){
      a = parseInt((i-1) / 3) 
      b = parseInt((i-1) % 3)
      keypad[i] = [a,b]
  }
  keypad["*"] = [3,0]
  keypad[0] = [3,1]
  keypad["#"] = [3,2]
}

const decideHand = (keypad, num, mainHand, location) => {

  if(keypad[num][1] === 0){
      location[0] = num
      return "L"
  }
  if(keypad[num][1] === 2){
      location[1] = num
      return "R"
  }
  let diffL,diffR
  diffL = Math.abs(keypad[num][0] - keypad[location[0]][0]) + Math.abs(keypad[num][1] - keypad[location[0]][1])
  diffR = Math.abs(keypad[num][0] - keypad[location[1]][0]) + Math.abs(keypad[num][1] - keypad[location[1]][1])
  if(diffL === diffR){
      if(mainHand === "left"){
          location[0] = num 
          return "L"
      }
      location[1] = num 
      return "R"
  }
  if(diffL < diffR){
      location[0] = num 
      return "L"
  }
  location[1] = num
  return "R" 
}

const solution = (numbers, hand) => {
  const keypad = {}
  makeKeypad(keypad)
  const location = ["*","#"]
  let answer = '';
  numbers.map((num) => answer += decideHand(keypad, num, hand, location))
  return answer;
}