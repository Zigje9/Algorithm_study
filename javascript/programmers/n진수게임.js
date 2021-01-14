function solution(n, t, m, p) {
  let gameString = ""
  for (let i=0 ; i<m*t ; i++){
      gameString += i.toString(n)
  }
  let answer = ""
  gameString.slice(p-1).split("").map((char, idx) => idx%m === 0 ? answer += char : 1)
  return answer.slice(0,t).toUpperCase()
}