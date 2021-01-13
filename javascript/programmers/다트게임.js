const checkSDT = (char) => {
  return (char === "S" || char === "D" || char === "T")
}

const checkOption = (char) => {
  return (char === "*" || char === "#")
}

const changeSDT = (char) => {
  if (char === "S") return 1
  if (char === "D") return 2
  if (char === "T") return 3
}

function solution(dartResult) {
  const answer = []
  const game = []
  let tempStr = ""
  let flag = true
  for (let i=0 ; i<dartResult.length ; i++){
      if(checkSDT(dartResult[i])){
          flag = false
      }
      if(!flag && !isNaN(dartResult[i])){
          game.push(tempStr.split(""))
          tempStr = ""
          flag = true
      }
      tempStr += dartResult[i]
      if(i === dartResult.length-1){
          game.push(tempStr.split(""))
      }
  }
  let count = 0
  game.map((dart) => {
      if(checkOption(dart[dart.length-1])){
          if(dart[1] === '0'){
              if(dart[3]==="*"){
                  answer.push(Math.pow(10,changeSDT(dart[2]))*2)
                  if(count!=0){
                      answer[count-1]*=2
                  }
              }
              else{
                  answer.push(Math.pow(10,changeSDT(dart[2]))*(-1))
              }
          }
          else{
              if(dart[2]==="*"){
                  answer.push(Math.pow(+dart[0],changeSDT(dart[1]))*2)
                  if(count!=0){
                      answer[count-1]*=2
                  }
              }
              else{
                  answer.push(Math.pow(+dart[0],changeSDT(dart[1]))*(-1))
              }
          }
      }
      else{
          if(dart[1] === '0'){
              answer.push(Math.pow(10,changeSDT(dart[2])))
          }
          else{
              answer.push(Math.pow(+dart[0],changeSDT(dart[1])))
          }
      }
      count ++
  })
  return answer.reduce((acc, cur) => acc+cur, 0)
}