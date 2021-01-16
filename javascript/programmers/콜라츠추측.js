function solution(num) {
    const recursive = (num, count) => {
        if (count === 501) return -1
        if (num === 1) return count
        if (num % 2 === 0) return recursive(num/2, ++count)
        return recursive(num*3+1, ++count)
    }
    return recursive(num, 0)
}