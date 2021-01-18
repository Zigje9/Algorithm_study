const getDiff = (front, back) => {
  return Math.abs(front.reduce((acc, cur) => acc+cur)-back.reduce((acc, cur) => acc+cur))
}

function solution(A) {
  let min = 9999999999
  let nowValue
  const size = A.length
  for (let i=0 ; i<size-1 ; i++){
      nowValue = getDiff(A.slice(0,i+1), A.slice(i+1, size))
      min > nowValue ? min = nowValue : 1
  }
  return min
}
// 배열을 두부분으로 나누어 차의 절대값의 최소를 찾는 문제
// slice를 사용해서 배열 두개로 나누어 하면 N^2의 복잡도로 퍼포먼스 0

function solution(A) {
  let min = "start"
  let leftValues = []
  let now = 0
  let total = A.reduce((acc, cur) => {
      leftValues.push(acc)
      return acc + cur
  })
  for (let i=0 ; i<leftValues.length ; i++){
      now = Math.abs(2*leftValues[i]-total)
      if(min === "start"){
          min = now
      }
      else{
          min < now ? 1 : min = now
      }
  }
  return min
}
// reduce 로 돌면서 left 합산값을 배열에 저장하고 배열을 돌면서 최소값 찾기 O(N)