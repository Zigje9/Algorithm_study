function solution(n) {
  const DP = Array.from(new Array(100001), () => [0]);
  const DIVIDER = 1234567;
  DP[0] = 0;
  DP[1] = 1;
  for (let i = 2; i < 100001; i++) {
    DP[i] = (DP[i - 1] % DIVIDER) + (DP[i - 2] % DIVIDER);
  }

  return DP[n] % DIVIDER;
}
