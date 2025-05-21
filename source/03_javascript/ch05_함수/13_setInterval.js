// 1000밀리세컨마다 콜백함수 수행
let id = setInterval(() => {
  console.log(new Date());
}, 1000);

// 일정시간 후(10초) 후 타이머 중지
setTimeout(() => {
  clearTimeout(id);
  console.log('타이머 끝');
}, 10000);
