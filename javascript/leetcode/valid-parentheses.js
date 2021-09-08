var isValid = function (s) {
  const b = {
    '(': -1,
    ')': 1,
    '{': -2,
    '}': 2,
    '[': -3,
    ']': 3,
  };

  const brackets = s.split('');
  const stack = [];

  for (let bracket of brackets) {
    if (b[bracket] < 0) {
      stack.push(bracket);
    } else {
      if (stack.length === 0) {
        return false;
      }
      if (b[stack[stack.length - 1]] + b[bracket] !== 0) {
        return false;
      }
      stack.pop();
    }
  }
  if (stack.length === 0) {
    return true;
  }
  return false;
};
