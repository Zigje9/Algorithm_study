function solution(A) {
  let count = 0
  for(let i=0 ; i<A.length-1 ; i++){
      for(let j=i+1 ; j<A.length ; j++){
          if(j-i<=A[i]+A[j]){
              count++
          }
      }
  }
  return count
}
//81%

function solution(A) {
  const memo = []
  A.map((val, idx) => {
      memo.push([idx-val, true])
      memo.push([idx+val, false])
  }) 
  memo.sort((a, b) => {
      if(a[0] === b[0]){
          return b[1] - a[1]
      }
      return a[0]-b[0]
  })
  let disc = 0
  let answer = 0
  memo.map((e) => {
      if(e[1]){
          answer += disc
          disc += 1
      }
      else{
          disc -= 1
      }
  })
  return answer > 10000000 ? -1 : answer
}
//100% lower,upper 값을 소팅하고 disc 값을 변경하면서 추가함 