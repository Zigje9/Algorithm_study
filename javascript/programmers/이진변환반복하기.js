const changeBinary = (string) => {
  let count = 0
  let nextStr = 0
  for (let str of string){
      str === '0' ? count += 1 : nextStr += 1
  }
  return [nextStr.toString(2), count]
}

function solution(s) {
  const answer = [0, 0]
  while(s !== '1'){
      let a, b
      [a, b] = changeBinary(s)
      s = a
      answer[1] += b
      answer[0] += 1
  }
  return answer;
}