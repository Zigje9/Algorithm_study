function solution(N) {
  let count = 0
  let answer = 0
  N.toString(2).split("").map(num => {
      if (num === "0") {
          count += 1
      }
      else{
          if (answer < count){
              answer = count
          }
          count = 0
      }
  })
  return answer
}
// 숫자를 입력받아 이진변환 후 연속된 0의 최댓값 구하기 