var strStr = function (haystack, needle) {
  function checkStr(index, M) {
    let j = index;
    let k = 0;
    while (k < M) {
      if (haystack[j] !== needle[k]) {
        return false;
      }
      j += 1;
      k += 1;
    }
    return true;
  }
  const N = haystack.length;
  const M = needle.length;
  for (let i = 0; i <= N - M; i++) {
    if (checkStr(i, M)) {
      return i;
    }
  }
  return -1;
};
