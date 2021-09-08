var removeDuplicates = function (nums) {
  const N = nums.length;
  if (N === 0) {
    return 0;
  }
  let i = 0;
  let j = 1;
  while (j < N) {
    if (nums[i] === nums[j]) {
      j += 1;
    } else {
      i += 1;
      nums[i] = nums[j];
      j += 1;
    }
  }
  return i + 1;
};
