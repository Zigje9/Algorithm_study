function solution(n, words) {
  const di = {}
  let nextC = ""
  for (const [idx, value] of words.entries()) {
      if (idx === 0){
          nextC = value[value.length-1]
          di[value] = true
          continue
      }
      if (nextC !== value[0] || di.hasOwnProperty(value)){
          return [(n+idx)%n+1, parseInt(idx/n+1)]
      }
      nextC = value[value.length-1]
      di[value] = true
  }
  return [0, 0];
}