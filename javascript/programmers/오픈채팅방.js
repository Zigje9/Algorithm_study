const openChat = (command, memory, answer) => {
    switch (command[0]){
        case "Enter":
            memory[command[1]] = command[2]
            answer.push([command[1], "님이 들어왔습니다."])
            break
        case "Leave":
            answer.push([command[1], "님이 나갔습니다."])
            break
        case "Change":
            memory[command[1]] = command[2]
            break
    }
}

function solution(record) {
    const memory = {}
    const answer = []
    record.map(str => openChat(str.split(" "), memory, answer))
    return answer.map(el => el=memory[el[0]]+el[1])
}