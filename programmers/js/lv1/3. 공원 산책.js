let answer = [];
const park = ["OSO","OOO","OXO","OOO"];
const routes = ["E 2","S 3","W 1"];

let start = [];
const parkSize = [park.length-1, park[0].length-1];
let blockList = [[]];

for(let i in park) {
    for(let j in park[i]) {
        switch(park[i][j]) {
            case 'S':
                start = [parseInt(i, 10), parseInt(j, 10)];
                answer = start;
                break;
            case 'X':
                blockList.push([parseInt(i, 10), parseInt(j, 10)]);
                break;
        }
    }
}

for(let i in routes) {
    const parts = routes[i].split(' ');
    const direction = parts[0];
    const cnt = parts[1];

    for(let i=0; i<cnt; i++) {
        switch(direction) {
            case 'E':
                if(answer[1] + 1 <= parSize[1]) {
                    break;
                }
                answer[1]++;
                break;
            case 'W':
                answer[1]--;
                break;
            case 'S':
                answer[0]--;
                break;
            case 'N':
                answer[0]++;
                break;
        }
        // size 체크
        // 장애물 체크
    }
    
}