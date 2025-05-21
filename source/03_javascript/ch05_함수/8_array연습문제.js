// 연습문제 : 아래와 같이 매개변수가 없으면 -999를 리턴하고 매개변수가 1개 이상이면 누적합을 리턴하는 가변인자 함수 sumAll()을 작성한 스크립트 파일을 이용하시오.
function sumAll() {
  result = 0;

  if (arguments.length == 0) {
    result = -999;
  } else if (arguments.length >= 1) {
    for (let data of arguments) {
      result += data;
    }
  }
  return result;
}

// console.log(
//   '매개변수의 합은 : ' +
//     new Date().getMinutes() +
//     '분 ' +
//     new Date().getMilliseconds() +
//     '초 / ' +
//     sumAll()
// );
// console.log(
//   '매개변수의 합은 : ' +
//     new Date().getMinutes() +
//     '분 ' +
//     new Date().getMilliseconds() +
//     '초 / ' +
//     sumAll(2)
// );
// console.log(
//   '매개변수의 합은 : ' +
//     new Date().getMinutes() +
//     '분 ' +
//     new Date().getMilliseconds() +
//     '초 / ' +
//     sumAll(1, 2)
// );
// console.log(
//   '매개변수의 합은 : ' +
//     new Date().getMinutes() +
//     '분 ' +
//     new Date().getMilliseconds() +
//     '초 / ' +
//     sumAll(1, 2, 3, 4, 5)
// );
// console.log(
//   '매개변수의 합은 : ' +
//     new Date().getMinutes() +
//     '분 ' +
//     new Date().getMilliseconds() +
//     '초 / ' +
//     sumAll(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
// );
