function solution(A) {
  const leftMember = new Map()
  const rightMember = new Map()
  let answer = 0
  A.map(e => {
      if(rightMember.has(e)){
          rightMember.set(e,rightMember.get(e)+1)
      }
      else{
          rightMember.set(e,1)
      }
  })
  
  let nowValue
  let leftLeader
  for (let i=0 ; i<A.length ; i++){
      nowValue = A[i]
      if(leftMember.has(nowValue)){
          leftMember.set(nowValue, leftMember.get(nowValue)+1)
      }
      else{
          leftMember.set(nowValue, 1)
      }
      rightMember.set(nowValue, rightMember.get(nowValue)-1)

      if(leftMember.get(nowValue) > (i+1)/2){
          leftLeader = nowValue
          if(rightMember.get(leftLeader) > (A.length-i-1)/2){
              answer++
          }
          continue
      }
      if(leftMember.get(leftLeader) > (i+1)/2){
          if(rightMember.get(leftLeader) > (A.length-i-1)/2){
              answer++
          }
      }
  }
  return answer
}
//오른쪽 맵에 key value를 저장해 놓고, 전체 루프를 돌면서 왼쪽 leader를 구하고 오른쪽 값을 계속변경