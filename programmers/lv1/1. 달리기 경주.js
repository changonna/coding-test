function solution(players, callings) {
  const idxList = {};
  
  // index값을 별도의 객체로 저장
  for(i in players) {
      idxList[players[i]] = i;
  }
  
  for(i in callings) {
      // 불려진 player의 index
      const playerRank = idxList[callings[i]];
      // 이전 player의 name
      const beforePlayer = players[playerRank-1];
      
      // players의 이전 플레이어와 불려진 플레이어 변경
      players[playerRank-1] = callings[i];
      players[playerRank] = beforePlayer;
    
      // index List의 각 플레이어의 index 값도 변경
      idxList[beforePlayer] = playerRank;
      idxList[callings[i]] = playerRank-1;
  }
  
  return players;
}