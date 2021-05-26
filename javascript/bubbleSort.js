const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7]

let temp = 0
for (let i=0 ; i<numList.length-1 ; i++){
  for (let j=0 ; j<numList.length-1-i ; j++){
    if(numList[j] > numList[j+1]){
      temp = numList[j]
      numList[j] = numList[j+1]
      numList[j+1] = temp
    }
  }
}

console.log(numList)