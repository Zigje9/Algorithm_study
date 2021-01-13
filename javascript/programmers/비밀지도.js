function solution(n, arr1, arr2) {
    const answer = [];
    for (let i=0 ; i<n ; i++){
        answer.push((arr1[i] | arr2[i]).toString(2).padStart(n,'0').replace(/1/g,"#").replace(/0/g," "))
    }
    return answer;
}
//비트연산후 정규식으로변경
//map 의 index를 사용하면 for문 없이 가능할것 ... map((ele, index) => ele & arr2[index]  ... ... ... )