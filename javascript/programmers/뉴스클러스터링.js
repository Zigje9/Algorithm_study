const changeArr = (arr) => {
  const newArray = []
  let reg = /[a-zA-Z]/
  for (let i=1 ; i<arr.length ; i++){
      if(reg.test(arr[i-1]) && reg.test(arr[i])) newArray.push((arr[i-1]+arr[i]).toUpperCase())
  }
  return newArray
}

const countIntersection = (arr1, arr2, size1, size2) => {
  let count = 0
  const check1 = new Array(size1).fill(0)
  const check2 = new Array(size2).fill(0)
  for (let i=0 ; i<size1 ; i++){
      for (let j=0 ; j<size2 ; j++){
          if(arr1[i] === arr2[j] && check2[j]==0){
              check1[i] = 1
              check2[j] = 1
              count ++ 
              break
          }
      }
  }
  return check1.reduce((acc, cur) => acc+cur)
}

function solution(str1, str2) {
  const arr1 = changeArr(str1)
  const arr2 = changeArr(str2)
  
  const size1 = arr1.length
  const size2 = arr2.length
  if(size1===0 || size2===0){
      if(size1===0 && size2===0){
          return 65536
      }
      return 0
  }
  
  let JA, JB
  size1 >= size2 
      ? JA = countIntersection(arr2, arr1, size2, size1) 
      : JA = countIntersection(arr1, arr2, size1, size2)
  JB = size1 + size2 - JA
  
  return parseInt(JA/JB*65536)
}