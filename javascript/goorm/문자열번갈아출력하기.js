const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const inputArray = []

const solution = (input) => {
	let answer = ""
	const strList = input.split("")
	const endCount = strList.length
	const centerCount = parseInt(strList.length/2)
	for (let i = 0 ; i<centerCount ; i++){
		answer += strList[i]
		answer += strList[endCount-i-1]
	}
	(endCount % 2) === 0 ? console.log(answer) : console.log(answer += strList[centerCount])   
} 

rl.on("line", function(line) {
	inputArray.push(line)
	rl.close();
}).on("close", function() {
	solution(inputArray[0])
	process.exit();
});