const changeDir = (dir) => {
  switch (dir){
      case 'down':
          dir = 'right'
          return dir
      case 'right':
          dir = 'up'
          return dir
      case 'up':
          dir = 'down'
          return dir
  }
}

const move = (dir, currX, currY) => {
  switch (dir){
      case 'down':
          return [1,0]
      case 'right':
          return [0,1]
      case 'up':
          return [-1,-1]
  }
}

function solution(n) {
  let lastNum = (n+1)*n/2
  let count = 1
  const top = Array.from(Array(n), () => new Array(count++).fill(0))
  let currX = 0
  let currY = 0
  let nowDir = 'down'
  let dirStack = n
  let dirCount = 0
  for (let i=1 ; i<=lastNum ; i++){
      top[currX][currY] = i
      dirCount++
      if(dirStack === dirCount){
          nowDir = changeDir(nowDir)
          dirStack -= 1
          dirCount = 0
      }
      currX+=move(nowDir, currX, currY)[0]
      currY+=move(nowDir, currX, currY)[1]
  }
  return top.flat()
}