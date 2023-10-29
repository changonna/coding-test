// 내 풀이
// function solution(name, yearning, photo) {
//   var answer = [];
//   const idxList = {};
  
//   // idxList 객체에 key를 name, value에 추억 점수를 저장
//   for(let i in name) {
//       idxList[name[i]] = yearning[i];
//   }
  
//   // photo 배열을 돌면서
//   for(let i in photo) {
//       let score = 0;
//       for(let j in photo[i]) {
//           // idxList key에 이름이 있으면 추억 점수를 추가 / 없으면 +0
//           score += idxList[photo[i][j]] ?? 0;
//       }
//       answer.push(score);
//   }

//   console.log(answer);
//   return answer;
// }



// 다른 사람의 풀이
function solution(name, yearning, photo) {
  return photo.map((v)=> v.reduce((a, c)=> a += yearning[name.indexOf(c)] ?? 0, 0));
}
// photo를 map 함수를 사용하여 전체 배열을 순회하며
// reduce 함수를 사용하여 해당 배열마다 name의 index를 가져와 yearning의 값을 더하거나 0을 더한다. (a의 초기값은 0)



/** 추가 공부
 * .map() 정의
 * .reduce() 정의
 * name.indexOf(c) ????
 */ 







// const name = ["may", "kein", "kain", "radi"];
// const yearning = [5, 10, 1, 3];
// const photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]];

const answer = solution(name, yearning, photo);
console.log(answer);