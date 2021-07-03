function solution(begin, target, words) {
  if (words.includes(target) === false) {
    return 0;
  }

  const visit = new Array(words.length).fill(false);

  function check(a, b) {
    let count = 0;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        count += 1;
        if (count > 1) {
          return false;
        }
      }
    }
    if (count === 1) {
      return true;
    }
    return false;
  }

  function bfs() {
    const q = [[begin, 0]];
    while (q.length > 0) {
      const [nowWord, nowCount] = q.shift();
      if (nowWord === target) {
        return nowCount;
      }
      words.forEach((nextWord, idx) => {
        if (visit[idx] === false) {
          if (check(nowWord, nextWord)) {
            q.push([nextWord, nowCount + 1]);
            visit[idx] = true;
          }
        }
      });
    }
    return 0;
  }
  return bfs();
}
