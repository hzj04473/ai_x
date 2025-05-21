// 클로저 함수 : return 된 함수
let test = (name) => {
  let msg = `Hello ${name}님 방가방가`;
  return () => console.log(msg);
};

// let funVar = test('홍길동');
// console.log(funVar());
test('홍길동')();
