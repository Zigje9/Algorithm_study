const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7];

function heapSort(nums) {
  for (let i = nums.length - 1; i >= 0; i--) {
    nums = heapifyDown(nums, i, nums.length - 1);
  }

  let temp = 0;
  for (let i = nums.length - 1; i >= 0; i--) {
    nums = heapifyDown(nums, 0, i);

    if (nums[0] > nums[i]) {
      temp = nums[i];
      nums[i] = nums[0];
      nums[0] = temp;
    }
  }
  return nums;
}

function heapifyDown(nums, k, leafIdx) {
  while (2 * k + 1 <= leafIdx) {
    let left = 2 * k + 1;
    let right;
    2 * k + 2 <= leafIdx ? (right = 2 * k + 2) : (right = 0);
    let m = k;
    let temp = 0;
    nums[left] > nums[k] ? (m = left) : (m = k);
    if (right !== 0) {
      nums[right] > nums[m] ? (m = right) : (m = m);
    }
    if (k !== m) {
      temp = nums[k];
      nums[k] = nums[m];
      nums[m] = temp;
      k = m;
    } else {
      break;
    }
  }
  return nums;
}

console.log(heapSort(numList));
