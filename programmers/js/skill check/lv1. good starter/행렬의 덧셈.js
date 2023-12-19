function solution(arr1, arr2) {
    let answer = [];

    for(let i in arr1) {
        let sum = [];
        for(let j in arr1[0]) {
            sum.push(arr1[i][j] + arr2[i][j]);
        }
        answer.push(sum);
    }

    return answer;
}
