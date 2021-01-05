const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const input = []

const solution = (array) => {
	const N = +array[0]
	const road = []
	const dp = Array.from(Array(N), () => new Array(N).fill(0))
	for (i=0 ; i<N ; i++){
		road.push(array[i+1].split(" ").map((el)=> +el))
	}
	console.log(dynamic(dp, road, N)[N-1][N-1])
}

const dynamic = (dp, data, num) => {
	dp[0][0] = data[0][0]
	for(let i=1 ; i<num ; i++){
		dp[0][i] = dp[0][i-1] + data[0][i]
	}
	for(let j=1 ; j<num ; j++){
		for(let i=0 ; i<num ; i++){
			if(i===0){
				dp[j][i] = data[j][i] + dp[j-1][i]
			}
			else{
				dp[j-1][i] > dp[j][i-1] ? dp[j][i]+=dp[j-1][i] : dp[j][i]+=dp[j][i-1]
				dp[j][i] += data[j][i]
			}
		}
	}
	return dp
}

rl.on("line", function(line) {
	input.push(line)
}).on("close", function() {
	solution(input)
	process.exit();
});