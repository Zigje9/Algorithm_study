class Node {
  constructor(ele, next = null) {
    this.ele = ele;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insertFront(ele) {
    const node = new Node(ele, this.head);
    this.head = node;
    this.size++;
  }

  insertBack(ele) {
    const node = new Node(ele, null);
    if (this.size === 0) {
      this.head = node;
      this.size++;
    } else {
      let cur = this.head;
      while (cur.next !== null) {
        cur = cur.next;
      }
      cur.next = node;
      this.size++;
    }
  }

  insert(ele, idx) {
    if (idx > this.size) {
      console.log('index error');
      return;
    }
    if (idx === this.size) {
      this.insertBack(ele);
      return;
    }
    if (idx === 0) {
      this.insertFront(ele);
      return;
    }
    let pre = this.head;
    let count = 1;
    while (count !== idx) {
      pre = pre.next;
      count += 1;
    }
    const node = new Node(ele, null);
    node.next = pre.next;
    pre.next = node;
    this.size++;
  }

  remove(idx) {
    if (idx > this.size - 1) {
      console.log('index error');
      return;
    }
    if (idx === 0) {
      this.head = this.head.next;
      this.size--;
    }
    let pre = this.head;
    let count = 0;
    while (count !== idx - 1) {
      pre = pre.next;
      count++;
    }
    if (idx === this.size - 1) {
      pre.next = null;
    } else {
      pre.next = pre.next.next;
    }
    this.size--;
  }

  printAll() {
    let cur = this.head;
    let count = this.size;
    while (cur !== null) {
      console.log(cur.ele, this.size - count);
      cur = cur.next;
      count--;
    }
  }
}

const linkedList = new LinkedList();
linkedList.insertBack('a');
linkedList.insertFront('b');
linkedList.insertFront('c');
linkedList.insertBack('d');
linkedList.insert('e', 2);
linkedList.insert('f', 0);
linkedList.insert('g', 3);
linkedList.insert('ppp', 7);
linkedList.insert('ppo', 4);
linkedList.remove(4);
linkedList.printAll();
