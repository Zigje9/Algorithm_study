function solution(orders, course) {
  orders = orders.map((e) => {
      return e.split("").sort().join("")
  })
  orders.sort()
  const di = {}
  const getCombination = (origin, str, n, r, count) => {
      if(r === 0){
          if(di.hasOwnProperty(str)){
              di[str][0] += 1
          }else{
              di[str] = [1, str.length]
          }
      }
      else if(n === 0 || n < r) return
      else { 
          str = (str+origin[count])
          getCombination(origin, str, n-1, r-1, count+1)
          str = str.slice(0,str.length-1)
          getCombination(origin, str, n-1, r, count+1)
      } 
  }
  orders.forEach((e) => {
      for(let r of course){
          if(r <= e.length){
              getCombination(e, "", e.length, r, 0)
          }
      }
  })
  const candi = {}
  for(let c of course){
      candi[c] = 0
  }
  for (const [key, value] of Object.entries(di)){
      if(value[0] > candi[value[1]]){
          candi[value[1]] = value[0]
      }
  }
  const answer = []
  for (const [key, value] of Object.entries(di)){
      if(value[0] >= 2){
          if(candi[value[1]] === value[0]){
              answer.push(key)
          }    
      }
  }
  answer.sort()
  return answer
}