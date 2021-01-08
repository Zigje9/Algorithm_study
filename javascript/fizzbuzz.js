// 1부터 100까지 3의 배수는 Fizz, 5의 배수는 Buzz, 15의 배수는 FizzBuzz 출력하기

for (let i=1 ; i<=100; i++){
  let str = ""
  i%3 === 0 ? str+="Fizz" : str
  i%5 === 0 ? str+="Buzz" : str
  console.log(i, str)
}

for (let i=1 ; i<=100 ; i++){
  console.log(i, (i%3===0?"Fizz":"")+(i%5===0?"Buzz":""))
}