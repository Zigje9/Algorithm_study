function solution(gems) {
  const di = {}
  gems.forEach((e) => {
      if(di.hasOwnProperty(e)){
          di[e] += 1
      }
      else{
          di[e] = 1
      }
  })
  let left = 0
  let right = gems.length-1
  while(left <= right){
      if(left === right){
          return [left+1, left+1]
      }
      
      if(di[gems[right]] == 1){
          break
      }
      else{
          di[gems[right]] -= 1
          right -= 1
      }
  }
  let answer = [left+1, right+1]
  let flag = true
  if(di[gems[left]] > 1){
      flag = true
  }
  else{
      flag = false
  }
  while(right <= gems.length-1){
      if(left === right){
          break
      }
      if(flag){
          di[gems[left]] -= 1
          left += 1
          if(di[gems[left]] > 1){
              flag = true
          }
          else{
              flag = false
          }
      }
      else{
          if(right + 1 === gems.legnth-1){
              break
          }
          right += 1
          di[gems[right]] += 1
          if(di[gems[right]] === di[gems[left]]){
              flag = true
          }
          else{
              flag = false
          }
      }
      if(answer[1]-answer[0]+1 > right-left+1){
          answer = [left+1, right+1]
      }
  }
  return answer
}