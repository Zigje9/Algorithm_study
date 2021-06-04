function closure1() {
  for (var i = 1; i <= 3; i++) {
    setTimeout(() => {
      console.log(i);
    }, 3000);
  }
}

function closure2() {
  for (let i = 1; i <= 3; i++) {
    setTimeout(() => {
      console.log(i);
    }, 3000);
  }
}

function closure3() {
  for (var i = 1; i <= 3; i++) {
    setTimeout(
      (function (i) {
        return function () {
          console.log(i);
        };
      })(i),
      3000
    );
  }
}

closure3();
