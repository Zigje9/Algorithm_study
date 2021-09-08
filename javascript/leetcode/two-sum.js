var twoSum = function (nums, target) {
  N = nums.length;
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};
