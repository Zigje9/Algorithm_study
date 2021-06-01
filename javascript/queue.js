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

class Queue {
  constructor() {
    this.stack1 = new Stack();
    this.stack2 = new Stack();
  }
  q_push(ele) {
    this.stack1._push(ele);
  }
  q_pop() {
    if (this.stack2._size() === 0) {
      if (this.stack1._size() === 0) {
        return null;
      }
      while (this.stack1._size() > 0) {
        this.stack2._push(this.stack1._pop());
      }
      return this.stack2._pop();
    } else {
      return this.stack2._pop();
    }
  }
}

const q = new Queue();
q.q_push('a');
q.q_push('b');
q.q_push('c');
console.log(q.q_pop());
q.q_push('d');
q.q_push('e');
console.log(q.q_pop());
q.q_push('f');
console.log(q);
