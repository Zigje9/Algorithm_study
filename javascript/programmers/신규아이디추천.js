const step1 = str => str.toLowerCase()

const step2 = str => {
    let reg = /[\{\}\[\]\/?,;:|\)*~`!^\+<>@\#$%&\\\=\(\'\"]/gi
    return str.replace(reg, "")
}

const step3 = str => {
    let temp = 0
    let nextStr = ""
    while (true) {
        temp = str.length
        if (temp === str.replace("..", ".").length) break
        str = str.replace("..", ".")
    }
    return str
}

const step4 = str => {
    if (str[0] === "." && str[str.length - 1] === ".") return str.slice(1, str.length - 1)
    if (str[0] === ".") return str.slice(1)
    if (str[str.length - 1] === ".") return str.slice(0, str.length - 1)
    return str
}

const step5 = str => {
    if (str.length === 0) return "a"
    return str
}

const step6 = str => {
    if (str.length >= 16) {
        str = str.slice(0, 15)
        return str[str.length - 1] === "." ? str.slice(0, str.length - 1) : str
    }
    return str
}

const step7 = str => {
    if (str.length <= 2) {
        return str.padEnd(3, str[str.length - 1])
    }
    return str
}
aa
function solution(new_id) {
    return step7(step6(step5(step4(step3(step2(step1(new_id)))))))
}