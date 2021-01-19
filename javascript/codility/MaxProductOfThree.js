function solution(A) {
  const ne = []
  const po = []
  A.sort((a, b) => a-b).map((e) => e<0 ? ne.push(e) : po.push(e))
  if(A.length === 3){
      return A[0]*A[1]*A[2]
  }
  if(ne.length === 0 || ne.length === 1){
      return po[po.length-1]*po[po.length-2]*po[po.length-3]
  }
  if(po.length === 0){
      return ne[ne.length-1]*ne[ne.length-2]*ne[ne.length-3]
  }
  if(po.length === 1){
      return po[0]*ne[0]*ne[1]
  }
  if(A.length === 4){
      return po[po.length-1]*ne[0]*ne[1]
  }
  return Math.max(po[po.length-1]*po[po.length-2]*po[po.length-3],po[po.length-1]*ne[0]*ne[1])
}
//3개의 곱의 최대값