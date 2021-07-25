function solution(data) {
  return deepCopy(data);
}

function deepCopy(obj) {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }
  if (Array.isArray(obj)) {
    const newObj = [];
    for (const key of Object.keys(obj)) {
      newObj[key] = deepCopy(obj[key]);
    }
    return newObj;
  }
  const newObj = {};
  for (const key of Object.keys(obj)) {
    newObj[key] = deepCopy(obj[key]);
  }
  return newObj;
}
