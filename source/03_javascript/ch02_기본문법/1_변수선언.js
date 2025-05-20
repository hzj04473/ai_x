// ! var : 변수선언시 사용. 변수 재선언 가능. 전역변수로 주로 사용.
v = 10;
var v = 20;

v++; // v를 1증가
++v;
v--; // v를 1감소
--v;
console.log(`v = ${v}`); // 터미널 열기 : ctrl+j, ctrl+~
// print('v=',str(v)) // python은 이렇게...

// ! let : 변수선언시 사용. 변수 재선언 불가. 블록{} 레벨 범위에서만 적용
let l;
l = 10;
// let l = 20; // 변수 재선언 불가
console.log(l);

// ! const : 상수 선언시 사용.
// const C = 20;
const C = [10, 20, 30]; // 배열
// C = 10; // TypeError: Assignment to constant variable.
console.log(C);
C[0] = 99; // 참조 주소는 변경을 할수는 없으나, 값은 변경 가능
console.log(C);
