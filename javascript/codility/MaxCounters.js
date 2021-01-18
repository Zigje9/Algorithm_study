function solution(N, A) {
  const answer = new Array(N).fill(0)
  let max = 0
  A.map((e) => {
      if(e > N){
          answer.map((el, idx) => answer[idx] = max)
      }
      else{
          answer[e-1] += 1
          if(max < answer[e-1]){
              max = answer[e-1]
          }
      }
  })
  return answer
}
// N개의 0으로 채워진 배열을 특정값에 따라 +1씩 추가하고 N보다 큰 index에서는 전체를 max 값으로 변경하는 배열을 리턴
// 퍼포먼스 40% O(N*M)의 복잡도를 가짐

function solution(N, A) {
  let max = 0
  let temp = 0
  const answer = new Array(N).fill(0)
  A.map(e => {
      if(e-1 >= N){
          temp = max
      }
      else{
          if(answer[e-1] < temp){
              answer[e-1] = temp
          }
          answer[e-1]++
          max = Math.max(answer[e-1], max)
      }
  })
  return answer.map((e, idx) => e < temp ? answer[idx]=temp : answer[idx])
}
// O(N+M) temp 에 변경할 최대값을 등록해놓고 실제로는 반영하지 않고 나중에 반영