function solution(N, road, K) {
  const graph = {}
  for(let i=1; i<=N; i++){
      graph[i] = {}
  }
  road.forEach((ele) => {
      let [left, right, dist] = ele
      if(graph[left].hasOwnProperty(right)){
          if(graph[left][right] > dist){
              graph[left][right] = dist
              graph[right][left] = dist
          }
      }
      else{
          graph[left][right] = dist
          graph[right][left] = dist
      }
  })
  
  function dijkstra(city, start){
      const route = {}
      for(const key of Object.keys(city)){
          route[key] = Number.MAX_SAFE_INTEGER
      }
      route[start] = 0
      
      const distArray = []
      distArray.push([route[start], start])
      
      while (distArray.length > 0){
          distArray.sort()
          const [nowDist, nowPos] = distArray.shift()
          if(route[nowPos] < nowDist){
              continue
          }
          for(const [nextPos, nextDist] of Object.entries(city[nowPos])){
              const changeDist = nowDist + nextDist
              if(changeDist < route[nextPos]){
                  route[nextPos] = changeDist
                  distArray.push([changeDist, nextPos])
              }
          }
      }
      return route
  }
  let answer = 0
  for(const value of Object.values(dijkstra(graph, 1))){
      K >= value ? answer += 1 : 1
  }
  
  return answer
}