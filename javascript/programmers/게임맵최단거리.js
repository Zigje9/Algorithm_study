function solution(maps) {
  const m = maps[0].length;
  const n = maps.length;
  const moveX = [0, 1, 0, -1];
  const moveY = [1, 0, -1, 0];

  const visit = Array.from(Array(n), () => new Array(m).fill(-1));

  function bfs(startX, startY) {
    visit[startX][startY] = 1;
    const q = [[startX, startY]];
    while (q.length) {
      const [nowX, nowY] = q.shift();
      for (let i = 0; i < 4; i++) {
        const nextX = nowX + moveX[i];
        const nextY = nowY + moveY[i];
        if (nextX >= 0 && nextX < n && nextY >= 0 && nextY < m) {
          if (visit[nextX][nextY] === -1 && maps[nextX][nextY] === 1) {
            q.push([nextX, nextY]);
            visit[nextX][nextY] = visit[nowX][nowY] + 1;
          }
        }
      }
    }
  }
  bfs(0, 0);
  return visit[n - 1][m - 1];
}
