function solution(m, musicinfos) {
    const N = musicinfos.length
    const music = musicinfos.map(e => e.split(","))
    const play = []

    const checkMusic = (origin, info) => {
        let idx = 0
        const ol = origin.length
        const il = info.length
        while(idx + ol<= il){
            if(origin[0] === info[idx]){
                if(origin.join("") === info.slice(idx, idx+ol).join("")){
                    return true
                }
            }
            idx += 1
        }
        return false
    }
    let mm = m + "X"
    let idx = 0
    const check = []
    while(true){
        if(mm[idx] === "X"){
            break
        }
        if(mm[idx+1] === "X"){
            check.push(mm[idx])
            break
        }
        if(mm[idx+1] === "#"){
            check.push(mm[idx]+mm[idx+1])
            idx += 2
            continue
        }
        check.push(mm[idx])
        idx += 1
    }
    music.forEach((e) => {
        const [fs, fe] = e[0].split(":")
        const [ss, se] = e[1].split(":")
        const time = Math.abs(((+fs*60)+(+fe)) - ((+ss*60)+(+se)))
        let temp = e[3]+"X"
        let idx = 0
        const mu = []
        while(true){
            if(temp[idx] === "X"){
                break
            }
            if(temp[idx+1] === "X"){
                mu.push(temp[idx])
                break
            }
            if(temp[idx+1] === "#"){
                mu.push(temp[idx]+temp[idx+1])
                idx += 2
                continue
            }
            mu.push(temp[idx])
            idx += 1
        }
        let recur = 0
        time > mu.length ? recur = parseInt(time/mu.length)+1 : recur = 1
        let real = []
        for(let i=0; i<recur ; i++){
            real = [...real, ...mu]
        }
        real = real.slice(0, time)
        if(checkMusic(check, real)){
            play.push([time, e[2]])
        }
    })
    if(play.length === 0){
        return "(None)"
    }
    play.sort((a, b) => b[0]-a[0])
    return play[0][1]
}