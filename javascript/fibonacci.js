function fibo1(num) {
  if (num <= 1) {
    return 1;
  }
  return fibo1(num - 1) + fibo1(num - 2);
}
console.log(fibo1(4));

function fibo2(num) {
  if (num <= 1) {
    return 1;
  }
  let a = 1;
  let b = 1;
  let result = 0;
  for (let i = 1; i < num; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}

console.log(fibo2(4));
