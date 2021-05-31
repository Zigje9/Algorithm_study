const array = [
  [1, 2, 3],
  [4, 5, 6],
];

const flatten = (arr) => {
  return arr.reduce((acc, cur) => {
    return acc.concat(cur);
  }, []);
};

const flatten2 = (arr) => {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result = [...result, ...arr[i]];
  }
  return result;
};

console.log(flatten(array));

console.log(flatten2(array));
