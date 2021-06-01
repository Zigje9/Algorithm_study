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

const stack = new Stack();
stack._push('a');
console.log(stack._pop());
stack._push('b');
stack._push('c');
console.log(stack._size());
console.log(stack._top());
console.log(stack);
