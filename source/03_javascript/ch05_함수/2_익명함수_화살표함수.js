let funVar = function (i, j) {
  console.log(`1. 매개변수 없는 일반 함수 호출`);
};
funVar();

funVar = (i, j) => {
  console.log(`2. 매개변수 없는 화살표 함수 호출`);
};
funVar();

funVar = function (i) {
  console.log(`3. 매개변수가 1개 있는 일발 함수 호출`);
  console.log(`매개변수 값 = ${i}`);
};
funVar(10);

funVar = (i) => {
  console.log(`4. 매개변수가 1개 있는 화살표 함수 호출`);
  console.log(`매개변수 값 = ${i}`);
};
funVar(10);

funVar = function (i) {
  console.log(`5. 매개변수가 하나의 한줄짜리 일반 함수 호출 매개변수는 ${i}`);
};
funVar(20);

funVar = (i) => console.log(`6. 매개변수가 하나의 한줄짜리 화살표 함수 호출 매개변수는 ${i}`);
funVar(20);

funVar = function (x) {
  return x * x;
};
console.log(`7. return 문만 있는 일반함수 호촐 ${funVar(10)}`);

funVar = (x) => x * x;
console.log(`8. return 문만 있는 화살표 함수 호촐 ${funVar(7)}`);

funVar = function (x, y) {
  return x * 10 + y;
};
console.log(`9. 매개변수가 2개가 있고, return 문장의 일반함수 호촐 ${funVar(5, 3)}`);

funVar = (x, y) => x * 10 + y;
console.log(`10. 매개변수가 2개가 있고, return 문장의 화살표 함수 호촐 ${funVar(5, 3)}`);

// 문제1)
var arr = [10, '홍길동', '신림동'];
// 일반함수
console.log(`\n일반함수`);
arr.forEach(function (data, idx) {
  console.log(`${idx} 번쨰 :  ${data}`);
});
console.log(`-------------------------`);
arr.forEach(function (data) {
  console.log(`${data}`);
});

// 화살표 함수
console.log(`\n화살표함수`);
arr.forEach((data, idx) => console.log(`${idx} 번쨰 :  ${data}`));
console.log(`-------------------------`);
arr.forEach((data) => console.log(`${data}`));
