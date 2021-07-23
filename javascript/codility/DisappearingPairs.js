function solution(S) {
  const stack = [];
  const arrS = S.split('');
  arrS.forEach((c) => (stack.length === 0 ? stack.push(c) : stack[stack.length - 1] === c ? stack.pop() : stack.push(c)));
  return stack.join('');
}
