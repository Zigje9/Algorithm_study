function solution(n, edge) {
  const graph = Array.from(Array(n), () => new Array());
  edge.forEach(([a, b]) => {
    graph[a - 1].push(b - 1);
    graph[b - 1].push(a - 1);
  });
  const visit = new Array(n).fill(false);
  const result = new Array(n).fill(0);
  let maxDist = 0;
  function bfs(start) {
    const q = [[start, 0]];
    visit[start] = true;
    while (q.length > 0) {
      const [nowNode, nowDist] = q.shift();
      if (graph[nowNode].length > 0) {
        graph[nowNode].forEach((nextNode) => {
          if (visit[nextNode] === false) {
            q.push([nextNode, nowDist + 1]);
            result[nextNode] = nowDist + 1;
            visit[nextNode] = true;
            if (nowDist + 1 > maxDist) {
              maxDist = nowDist + 1;
            }
          }
        });
      }
    }
  }
  bfs(0);
  return result.filter((e) => e === maxDist).length;
}
