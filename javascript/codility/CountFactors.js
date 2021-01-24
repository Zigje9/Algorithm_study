function solution(N) {
  let T = 1
  let count = 0
  while(T<Math.sqrt(N)){
      if(N%T === 0){
          count += 2
      }
      T++
  }
  if(T*T === N){
      count ++
  }
  return count
}
// 약수의 개수 