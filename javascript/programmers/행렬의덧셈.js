function solution(arr1, arr2) {
  const answer = []
  for(let i=0 ; i<arr1.length ; i++){
      answer.push(arr1[i].map((e, idx) => {
          return e+=arr2[i][idx]
      }))
  }
  return answer
}