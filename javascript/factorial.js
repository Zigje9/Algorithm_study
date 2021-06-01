const factorial = (num) => (num === 1 ? 1 : num * factorial(num - 1));

console.log(factorial(5));

class Stack {
  constructor() {
    this.top = -1;
    this.data = [];
  }
  _push(ele) {
    this.top++;
    this.data[this.top] = ele;
  }
  _pop() {
    if (this.top === -1) {
      return null;
    }
    return this.data[this.top--];
  }
  _top() {
    if (this.top === -1) {
      return null;
    }
    return this.data[this.top];
  }
  _size() {
    return this.top + 1;
  }
}

const factorial2 = (num) => {
  const s = new Stack();
  for (let i = num; i > 0; i--) {
    s._push(i);
  }
  let answer = 1;
  while (s._size() > 0) {
    answer *= s._pop();
  }
  return answer;
};

console.log(factorial2(5));
