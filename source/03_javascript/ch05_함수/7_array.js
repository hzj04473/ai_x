// array함수 : 가변인자함수(파이썬에서 튜플매개변수)
/**
 * 매개변수가 0개 : length가 0인 배열 생성 return
 * 매개변수가 1개 : length가 매개변수만큼의 크기인 배열 생성 return
 * 매개변수가 2개 이상 : 매개변수로 배열을 생성 return
 */

function array() {
  // arguments(매개변수 배열)에 매개변수 내용이 들어옴
  console.log(arguments, arguments.length);
  let result = [];

  if (arguments.length == 1) {
    // result = arguments[0] 만큼의 크기인 배열
    for (let cnt = 1; cnt <= arguments[0]; cnt++) {
      result.push(null);
    }
  } else if (arguments.length >= 2) {
    // result = arguments의 내용으로 배열
    // forEach 문은 되지 않는다. arguments.forEach() X

    for (let data of arguments) {
      result.push(data);
    }
    // for (let cnt = 0; cnt < arguments.length; cnt++) {
    //   result.push(arguments[cnt]);
    // }
  }
  return result;
}

let arr1 = array();
let arr2 = array(3);
let arr3 = array(1, 2, '삼');
console.log(arr1);
console.log(arr2);
console.log(arr3);

// let arr1 = array();
// let arr2 = array(2);
// let arr3 = array(2, 3, '사');
