console.log(pow(9, 3));
// 선언된 매개변수보다 많은 매개변수로 호출, 이하는 무시
console.log(pow(5, 2, 12, 10, 5));
// 선언된 매개변수보다 적은 매개변수로 호출
console.log(pow(5));
console.log(pow());

function pow(x, y) {
  // x의 y승을 return
  console.log(`함수내의 x = ${x}, y = ${y}`);

  result = 1;

  for (let cnt = 1; cnt <= y; cnt++) {
    result *= x;
  }

  // return result; // return이 없으면 undefined로 받음
}
