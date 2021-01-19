function solution(A) {
  const B = A.slice()
  const size = A.length
  let max = 0
  let temp = 1
  if(size === 0){
      return -1
  }
  if(size === 1){
      return 0
  }
  A.sort((a,b) => a-b)
  for(let i=1 ; i<size ; i++){
      if(A[i-1]===A[i]){
          temp += 1
      }
      else{
          temp = 1
      }
      if(max < temp){
          max = temp
          answer = A[i]
      }
  }
  if (max > size/2){
      return B.indexOf(answer)  
  }
  return -1
}
//깊은 복사로 배열 저장해놓고, 소팅 후 과반수 초과값 인덱스 찾기