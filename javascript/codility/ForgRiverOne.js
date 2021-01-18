function solution(X, A) {
  let count = 0 
  let answer = -1
  const record = {}
  A.map((val, idx) => {
      if(!record[val]){
          record[val] = true
          count ++
          if(count === X) {
          answer = idx
          }
      }
  })
  return answer
}
// A에 값 X보다 작거나 같은 숫자 배열이 들어오고, A의 처음부터 시작하여 X보다 작거나같은 모든 정수가 한번씩 나타날때의 최소 idx 찾기 만약 없으면 -1 리턴
