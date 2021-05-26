const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7]

let temp = 0
for (let i=1 ; i<numList.length ; i++){
  for (let j=i ; j>0 ; j--){
    if(numList[j-1] > numList[j]){
      temp = numList[j-1]
      numList[j-1] = numList[j]
      numList[j] = temp
    }
    else{
      break
    }
  }
}

console.log(numList)