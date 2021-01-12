function solution(arr) {
  const answer = [0,0]
  const startArr = arr.flat()
  const recursive = (recurArray) => {
      let checkLen = recurArray.length
      if (checkLen === 1){
          if (recurArray[0]===0){
              answer[0] += 1
              return
          }
          answer[1] += 1
          return
      }
      let checkValue = recurArray.reduce((acc, cur) => acc + cur, 0)
      if (checkLen === checkValue){
          answer[1] += 1
          return
      }
      if (checkValue === 0){
          answer[0] += 1
          return 
      }
      let arr1 = []
      let arr2 = []
      let arr3 = []
      let arr4 = []
      let size = recurArray.length
      const tempSize = Math.sqrt(size)
      for (let i=0 ; i<tempSize/2 ; i++){
          arr1=[...arr1,...recurArray.slice(i*tempSize, i*tempSize+tempSize/2)]
          arr2=[...arr2,...recurArray.slice(i*tempSize+tempSize/2, i*tempSize+tempSize)]
      }
      for (let i=tempSize/2 ; i<tempSize ; i++){
          arr3=[...arr3,...recurArray.slice(i*tempSize, i*tempSize+tempSize/2)]
          arr4=[...arr4,...recurArray.slice(i*tempSize+tempSize/2, i*tempSize+tempSize)]
      }
      recursive(arr1)
      recursive(arr2)
      recursive(arr3)
      recursive(arr4)
  }
  recursive(startArr)
  return answer;
}
// 2중배열로 처리하기?.. 배열쉽게쪼개기? 