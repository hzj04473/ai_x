let id = setTimeout(() => {
  console.log(`3초가 지났다.`);
}, 3000);

let cnt = 0; // while문 수행횟수
let nowTime = new Date().getTime(); // 현재의 밀리세컨
// console.log(nowTime);
while (new Date().getTime() < nowTime + 2000) {
  cnt++;
}

console.log('2초동안 cnt가 ' + cnt + ' 번 while문 반복 수행');
// settimeout 중지
clearTimeout(id);
console.log(' ~ 타이머 중지됨');
