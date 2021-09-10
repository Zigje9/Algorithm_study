var plusOne = function (digits) {
  digits.unshift(0);
  digits[digits.length - 1] += 1;
  for (let i = digits.length - 1; i > 0; i--) {
    if (digits[i] >= 10) {
      digits[i - 1] += 1;
      digits[i] -= 10;
    } else {
      break;
    }
  }
  if (digits[0] === 0) {
    return digits.slice(1);
  }
  return digits;
};
