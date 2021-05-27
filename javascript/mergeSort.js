const numList = [3, 6, 5, 9, 1, 4, 2, 8, 7];

function mergeSort(nums) {
  if (nums.length < 2) {
    return nums;
  }
  const mid = Math.floor(nums.length / 2);
  const left = nums.slice(0, mid);
  const right = nums.slice(mid);
  return merge(mergeSort(left), mergeSort(right));

  function merge(left, right) {
    const resultArray = [];
    let leftIdx = 0;
    let rightIdx = 0;
    while (leftIdx < left.length && rightIdx < right.length) {
      if (left[leftIdx] < right[rightIdx]) {
        resultArray.push(left[leftIdx]);
        leftIdx++;
      } else {
        resultArray.push(right[rightIdx]);
        rightIdx++;
      }
    }
    return resultArray.concat(left.slice(leftIdx), right.slice(rightIdx));
  }
}
console.log(mergeSort(numList));
