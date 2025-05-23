let arr1 = new Array('hig', 'abc', 'zzz', 'aaa'); // let arr1 = ['hig','abc','zzz','aaa'];
let arr2 = [52, 100, 12, 94];

let arr1copy = arr1.slice(); // 깊은복사
arr1copy = Array.from(arr1); //깊은복사
arr1copy = [...arr1]; //깊은복사

console.log('정렬전 arr1 : ' + arr1);
arr1.sort(); // ascii 코드 순으로 정렬
console.log('정렬후 arr1 : ' + arr1);

console.log('정렬전 arr2 : ' + arr2);
arr2.sort(); // 문자로 변환한 후 ascii 코드 순으로 정렬
console.log('ascii 코드 정렬후 arr2 : ' + arr2); // ascii 코드 정렬후 arr2 : 100,12,52,94

arr2.sort((left, right) => left - right); // 오름차순으로 정렬
console.log(`숫자 정렬후 : ${arr2}`);
arr2.sort((left, right) => right - left); // 내림차순으로 정렬
console.log(`숫자 정렬후 : ${arr2}`);

arr2.reverse();
console.log(`reverse 후 arr2 : ${arr2}`);

// 값이 큰 top3만 출력
arr2.sort((left, right) => right - left);
console.log(`top3 : ${arr2.slice(0, 3)}`);
