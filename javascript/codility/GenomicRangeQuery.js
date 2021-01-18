// A,C,G,T 가 1,2,3,4의 값을 갖는다. 배열의 인덱스 범위가 주어지고 그사이에 최소값을 저장

// solution1 (62%, perfomance 0%)
const change = (char) => {
  switch (char){
      case "A":
          return 1
          break
      case "C":
          return 2
          break
      case "G":
          return 3
          break
      case "T":
          return 4
          break

  }
}

function solution(S, P, Q) {
  const dna = S.split("").map((e) => change(e))
  const answer = []
  P.map((e, idx) => {
      let min = 4
      for(let i=e ; i<Q[idx]+1 ; i++){
          min > dna[i] ? min = dna[i] : min
      }
      answer.push(min)
  })
  return answer
}

//solution 2 (100%) a,c,g 배열에 누적변화를 만들고 idx값 차를 통해 변화 체크
const change = (a,c,g, char, idx) => {
  switch (char){
      case "A":
          a.push(a[idx-1]+1)
          c.push(c[idx-1])
          g.push(g[idx-1])
          break
      case "C":
          a.push(a[idx-1])
          c.push(c[idx-1]+1)
          g.push(g[idx-1])
          break
      case "G":
          a.push(a[idx-1])
          c.push(c[idx-1])
          g.push(g[idx-1]+1)
          break
      case "T":
          a.push(a[idx-1])
          c.push(c[idx-1])
          g.push(g[idx-1])
          break
  }
}

function solution(S, P, Q) {
  const a = [0]
  const c = [0]
  const g = [0]
  for(let i=0 ; i<S.length ; i++){
      change(a,c,g, S[i], i+1)
  }
  const answer = []
  for(let i=0 ; i<P.length ; i++){
      if(a[Q[i]+1]-a[P[i]]>0){
          answer.push(1)
          continue
      }
      if(c[Q[i]+1]-c[P[i]]>0){
          answer.push(2)
          continue
      }
      if(g[Q[i]+1]-g[P[i]]>0){
          answer.push(3)
          continue
      }
      answer.push(4)
  }
  return answer
}