function solution(number, k) {
  const stack = [];
  const n = number.length;
  let idx = 0;
  while (idx < n) {
    if (stack.length === 0) {
      stack.push(number[idx]);
      idx += 1;
      continue;
    }
    if (stack[stack.length - 1] >= number[idx]) {
      stack.push(number[idx]);
      idx += 1;
      continue;
    } else {
      stack.pop();
      k -= 1;
    }
    if (k === 0) {
      break;
    }
  }
  if (k === 0) {
    return stack.join('') + number.slice(idx);
  }
  return stack.join('').slice(0, n - k);
}
