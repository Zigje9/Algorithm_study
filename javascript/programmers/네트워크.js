function solution(n, computers) {
  let answer = 0;
  const graph = Array.from(Array(n), () => new Array());

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i !== j) {
        if (computers[i][j] === 1) {
          graph[i].push(j);
        }
      }
    }
  }

  const visit = new Array(n).fill(false);

  function bfs(x) {
    visit[x] = true;
    const q = [x];
    while (q.length > 0) {
      let nowComputer = q.shift();
      if (graph[nowComputer].length > 0) {
        graph[nowComputer].forEach((nextComputer) => {
          if (visit[nextComputer] === false) {
            visit[nextComputer] = true;
            q.push(nextComputer);
          }
        });
      }
    }
  }
  for (let i = 0; i < n; i++) {
    if (visit[i] === false) {
      bfs(i);
      answer += 1;
    }
  }

  return answer;
}
