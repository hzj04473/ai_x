// 변수 선언서 var(전역변수), let(지역변수), const(상수)
sum = 0;

for (let i = 1; i <= 5; i++) {
  sum += i;
  console.log('i = ' + i + ' 일떄 까지 누적합은 ' + sum);
}

console.log('for문 끝');
// console.log('i = ' + i + ' 일떄 까지 누적합은 ' + sum);
