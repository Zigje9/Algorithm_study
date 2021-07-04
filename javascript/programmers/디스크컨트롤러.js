function solution(jobs) {
  let time = 0;
  let total = 0;
  let count = 0;
  const n = jobs.length;
  const priorityQ = [];
  jobs.sort((a, b) => a[1] - b[1]).sort((a, b) => a[0] - b[0]);
  jobs.map((e) => e.push(false));
  time += jobs[0][0] + jobs[0][1];
  total += jobs[0][1];
  count += 1;
  jobs[0][2] = true;
  while (count < n) {
    console.log(time, total);
    for (let i = 0; i < n; i++) {
      if (jobs[i][0] > time) {
        break;
      }
      if (jobs[i][2] === false) {
        priorityQ.push([jobs[i][0], jobs[i][1]]);
        jobs[i][2] = true;
      }
    }
    if (priorityQ.length === 0) {
      for (let i = 0; i < n; i++) {
        if (jobs[i][2] === false) {
          priorityQ.push([jobs[i][0], jobs[i][1]]);
          jobs[i][2] = true;
          break;
        }
      }
    }
    priorityQ.sort((a, b) => a[1] - b[1]);
    const [start, ing] = priorityQ.shift();
    if (start <= time) {
      total += time - start + ing;
      time += ing;
    } else {
      total += ing;
      time = start + ing;
    }
    count += 1;
  }

  return parseInt(total / n);
}
