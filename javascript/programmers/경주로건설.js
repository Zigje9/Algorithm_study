function solution(board) {
  const N = board.length
  const moveX = [-1, 0, 1, 0] //up right down left
  const moveY = [0, 1, 0, -1]

  const visit = Array.from(Array(N), () => new Array(N).fill(-1))

  const bfs = () => {
      const q = []
      q.push([0, 0, "start", 0])
      visit[0][0] = 0
      while(q.length > 0){
          let [nowX, nowY, before, cost] = q.shift()
          for(let i=0 ; i<4 ; i++){
              const nextX = nowX + moveX[i]
              const nextY = nowY + moveY[i]
              if(0 <= nextX && nextX < N && 0 <= nextY && nextY < N){
                  if(!(nextX === 0 && nextY === 0) && board[nextX][nextY] === 0){
                      if(before === "start"){
                          q.push([nextX, nextY, i, 100])
                          visit[nextX][nextY] = 100
                          continue
                      }
                      let addCost = 100
                      if(before !== i){
                          addCost = 600
                      }
                      if(visit[nextX][nextY] === -1){
                          q.push([nextX, nextY, i, cost+addCost])
                          visit[nextX][nextY] = cost+addCost
                      }
                      else{
                          if(visit[nextX][nextY] >= cost+addCost){
                              q.push([nextX, nextY, i, cost+addCost])
                              visit[nextX][nextY] = cost+addCost
                          }
                      }
                  }   
              }
          }
      }
  }
  bfs()
  return visit[N-1][N-1]
}