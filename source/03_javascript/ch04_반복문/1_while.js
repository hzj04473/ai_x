/*
  while(조건) {
    반복할 명령어들;
  }


  do {
    반복할 명려어들;
  } while(조건);

  1초동안 while문을 몇번 실행했는지 출력
*/

const now = new Date();
var startTime = now.getTime();
// console.log(startTime);
// while (이 시점의 currentmillsec가 startTime_100이하냐){}
cnt = 0;
// while (new Date().getTime() < startTime + 1000) {
//   cnt++;
// }
// console.log(`while문 반복 횟수 : ${cnt}`);

do {
  ++cnt;
} while (new Date().getTime() < startTime + 1000);
console.log(`do ~ while문 반복 횟수 : ${cnt}`);
