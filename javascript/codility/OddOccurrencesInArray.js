function solution(A) {
  const answer = []
  let idx = 0
  A.map(e => {
      if(answer.includes(e)){
          idx = answer.indexOf(e)
          answer.splice(idx, 1)
      }
      else{
          answer.push(e)
      }
  })
  return answer[0]
}
// N^2 으로 시간초과.. 

function solution(A) {
    let answer = 0
    const dictionary = {}
    A.map(el => {
        if(!dictionary[el]){
            dictionary[el] = 1
        }
        else{
            ++dictionary[el]
        }
    })
    Object.keys(dictionary).map(e => {
        if(dictionary[e] % 2 === 1){
            answer = +e
        }
    })
    return answer
}
//total score 88% ... 