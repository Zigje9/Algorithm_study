var maxSubArray = function (nums) {
  let maxValue = nums[0];
  let prefix = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (prefix >= 0) {
      prefix += nums[i];
    } else {
      prefix = nums[i];
    }
    if (prefix > maxValue) {
      maxValue = prefix;
    }
  }
  return maxValue;
};
