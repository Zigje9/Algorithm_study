const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7];

// not in-place, stable
function quickSort1(nums) {
  if (nums.length <= 1) {
    return nums;
  }

  const pivot = nums[0];
  const left = [];
  const right = [];
  const same = [];

  nums.forEach((n) => {
    if (n < pivot) {
      left.push(n);
    } else if (n > pivot) {
      right.push(n);
    } else {
      same.push(n);
    }
  });

  return [].concat(quickSort1(left), same, quickSort1(right));
}

// console.log(quickSort1(numList));

// in-place
function quickSort2(nums, left, right) {
  if (left >= right) {
    return;
  }

  const mid = Math.floor((left + right) / 2);
  const pivot = nums[mid];
  const partition = divide(nums, left, right, pivot);

  quickSort2(nums, left, partition - 1);
  quickSort2(nums, partition, right);

  function divide(nums, left, right, pivot) {
    while (left <= right) {
      while (nums[left] < pivot) {
        left += 1;
      }
      while (nums[right] > pivot) {
        right -= 1;
      }
      if (left <= right) {
        let temp = nums[right];
        nums[right] = nums[left];
        nums[left] = temp;
        right -= 1;
        left += 1;
      }
    }
    return left;
  }
  return nums;
}

console.log(quickSort2(numList, 0, numList.length - 1));
