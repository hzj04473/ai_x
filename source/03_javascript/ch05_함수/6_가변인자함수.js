// 가변인자함수 : 매개변수의 갯수에 따라 변하는 함수. 화살표함수에서는 불가
// 내장함수 : Array()

let arr1 = [1, 2, '상'];
let arr2 = Array(1, 2, '상');

let arr3 = [, ,]; // 방의 갯수가 2인 빈 배열
let arr4 = Array(2);

let arr5 = []; // 방의 갯수가 0인 배열
let arr6 = Array();

console.log(arr1, arr1.length);
console.log(arr2, arr2.length);
console.log(arr3, arr3.length);
console.log(arr4, arr4.length);
console.log(arr5, arr5.length);
console.log(arr6, arr6.length);
