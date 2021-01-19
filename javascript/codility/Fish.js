function solution(A, B) {
  const river = []
  for(i=0 ; i<A.length ; i++){
      river.push([A[i],B[i]])
      while(1){
          if(river.length===1){
              break
          }
          if(river[river.length-2][1] === 1 && river[river.length-1][1] === 0){
              if(river[river.length-2][0] > river[river.length-1][0]){
                  river.pop()
              }
              else{
                  let temp = river[river.length-1]
                  river.pop()
                  river.pop()
                  river.push(temp)
              }
          }
          else{
              break
          }
      }
  }
  return river.length
}
//stack 으로 물고기 제거 