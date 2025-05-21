fun(); // 선언적 함수 정의 위에서도 호출 가능

// 선언적 함수
function fun() {
  console.log(`함수 fun`);
}

fun();

// 선언적 함수의 재정의 : 맨 마지맛에 정의 함수가 유효
function fun() {
  console.log('수정된 함수');
}

fun();
