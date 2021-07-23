function solution(A) {
  return new Set(A.map((num) => (num < 0 ? -num : num))).size;
}
