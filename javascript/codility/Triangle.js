function solution(A) {
  A.sort((a,b)=>b-a)
  for (let i=0 ; i<A.length-2 ; i++){
      if(A[i]<A[i+1]+A[i+2]){
          return 1
      }
  }
  return 0
}