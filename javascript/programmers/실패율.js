const getFail = (num, stages) => {
  let fails = 0
  let total = 0
  stages.map(el => el >= num ? el === num ? fails +=1 : total +=1 : 1)
  return fails/(total+fails)
}

function solution(N, stages) {
  const answer = []
  for (let i=1 ; i<=N ; i++){
      answer.push([i, getFail(i, stages)])
  }
  return answer.sort((a, b) => b[1]-a[1]).map(el => el[0])
}