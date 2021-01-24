function solution(nums) {
  const size = nums.length/2
  const setArray = [...new Set(nums)]
  if(size <= setArray.length){
      return size
  }
  return setArray.length
}
