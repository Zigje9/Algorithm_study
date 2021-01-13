const boom = (board, m, n) => {
  const check = new Array(m).fill().map(() => new Array(n).fill(0))
  let doll = ""
  for (let i=0 ; i<m-1 ; i++){
      for (let j=0 ; j<n-1 ; j++){
          doll = board[i][j]
          if (doll === board[i+1][j] & doll === board[i][j+1] & doll === board[i+1][j+1] & doll !== '💣'){
              check[i][j] = 1
              check[i+1][j] = 1
              check[i][j+1] = 1
              check[i+1][j+1] = 1
          }
      }
  }    
  for (let i=0 ; i<m ; i++){
      for (let j=0 ; j<n ; j++){
          if(check[i][j] === 1){
              board[i][j] = '💣'
          }
      }
  }
  return board
}

const drop = (board, m, n) => {
  for (let i=0 ; i<n ; i++){
      let stack = []
      for (let j=0 ; j<m ; j++){
          if(board[j][i] !== '💣'){
              stack.push(board[j][i])   
          }
      }
      for (let j=m-1 ; j>=0 ; j--){
          if(stack.length !== 0){
              board[j][i] = stack.pop()
          }
          else{
              board[j][i] = '💣'
          }
      }
  }
  return board
}

const count = (board) => {
  let result = 0
  board.map((line) => line.map((el) => el === '💣' ? result += 1 : 1))
  return result
}
  
function solution(m, n, board) {
  let answer = 0;
  let checkValue = 0;
  let newBoard = board.map((line) => line.split(""))
  while(true){
      newBoard = boom(newBoard, m, n)
      newBoard = drop(newBoard, m, n)
      checkValue = count(newBoard) 
      if (answer === checkValue) break
      answer = checkValue
  }
  return answer;
}