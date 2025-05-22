let arr = ['홍길동', 20];
for (let idx in arr) {
  console.log(`arr: ${idx} : ${arr[idx]}`);
}

let obj = { name: '홍길동', age: 20 }; // for~in문만 사용 가능
for (let key in obj) {
  console.log(`obj : ${key} : ${obj[key]}`);
}
obj.address = '서울시 관악구';
obj.hobby = '집가서 열공하기';
console.log('--obj에 속성 추가한 후--');
for (let key in obj) {
  console.log(`obj : ${key} : ${obj[key]}`);
}

delete obj.hobby; // 객체 속성 삭제
console.log('--obj에 속성 삭제한 후--');
for (let key in obj) {
  console.log(`obj : ${key} : ${obj[key]}`);
}
// console.log(obj);
