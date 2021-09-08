var searchInsert = function (nums, target) {
  function binarySearch(t) {
    let left = 0;
    let right = nums.length - 1;
    let mid;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (nums[mid] > target) {
        right = mid - 1;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
    return left;
  }
  if (target <= nums[0]) {
    return 0;
  }
  if (target > nums[nums.length - 1]) {
    return nums.length;
  }
  return binarySearch(target);
};
