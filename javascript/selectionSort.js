const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7]

let min
let minIdx

for(let i=0 ; i<numList.length ; i++){
  min = numList[i]
  minIdx = i
  for(let j=i+1 ; j<numList.length ; j++){
    if(min > numList[j]){
      min = numList[j]
      minIdx = j
    }
  }
  if(minIdx !== i){
    temp = numList[i]
    numList[i] = min
    numList[minIdx] = temp
  }
}

console.log(numList)
