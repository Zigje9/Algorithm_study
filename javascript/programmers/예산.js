function solution(d, budget) {
    let answer = 0
    let count = 0
    for (let money of d.sort((a,b)=> a-b)){
        if (budget < count+money){
            break
        }
        count+=money
        answer++
    }
    return answer
}

// sort() ASCII로 정렬
// sort((a, b) => a-b) 오름차순