function solution(A, K) {
  const size = A.length
  return [...A.slice(size-K%size, size), ...A.slice(0, size-K%size)]
}
// 배열을 K번 오른쪽으로 밀어서 새로운 배열을 리턴 