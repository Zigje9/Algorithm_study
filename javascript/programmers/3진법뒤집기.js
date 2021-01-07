function solution(n) {
    return n.toString(3).split("").reduce((acc,cur,idx) => +acc +cur*(Math.pow(3,idx)),[0])
}

//parseInt 를 사용하면 간단히 스트링에서 처리 가능할 것 
//고차함수 활용하기