/**
 * ※ 정규표현식
1. 참조 : 위키백과
2. 간략한 문법 : 
    \d     (숫자와 매치, [0-9]와 동일)
    \D     (숫자가 아닌것)
    \w     (영문자나 숫자, [a-zA-Z0-9])
    \W     (영문자나 숫자가 아닌 문자)

    .      (문자)
    \.     (. 의미)
    \-     (- 의미)
    {2, 4} (2~4번 반복)
    {4}    (4번 반복)
    {2,}   (2번이상 반복)
    +      (1번이상 반복)
    *      (0번이상 반복)
    ?      (0번이나 1번 반복)
 */

var str = 'abcd@ef';
// 패턴
let patternNum = /[0-9]/; /* 숫자 /정규표현식/ : 정규표현식 리터럴 */
let patternEng = /[a-zA-Z]/; /* 영문 */
let patternKor = /[가-힣ㄱ-하-ㅣ]/; /* 한글 */
var patternSpc = /[~`!@#$%^&*()_\-+=\|\\\[\]{}'":;?\/<>,\.]/; // 특수문자 정규표현식

// 정규표현식.test(str) : str에 정규표현식 패턴이 포함되었는지 여부(true/false)
console.log(`str에 숫자가 포함? : ${patternNum.test(str)}`);
console.log(`str에 영문자가 포함? : ${patternEng.test(str)}`);
console.log(`str에 한글 포함? : ${patternKor.test(str)}`);
console.log(`str에 특수문자 포함? : ${patternSpc.test(str)}`);

// str.match(정규표현식) - str이 정규표현식과 일치하면 : 정규표현식과 일치하는 문자 return
// str이 정규표현식과 일치하지 않으면 null return

let tel1 = '010-9999-9999';
let tel2 = '019-9999-9';
let patternTel = /^[0-9]{2,3}-[0-9]{3,4}-([0-9]{2}){2}$/;
console.log(`tel1 : ${tel1.match(patternTel)}`);
console.log(`tel2 : ${tel2.match(patternTel)}`);

if (tel1.match(patternTel)) {
  console.log(`tel은 전화번호 형식입니다.`);
} else {
  console.log(`tel은 전화번호 형식이 아닙니다.`);
}

if (tel2.match(patternTel)) {
  console.log(`tel은 전화번호 형식입니다.`);
} else {
  console.log(`tel은 전화번호 형식이 아닙니다.`);
}

// 전화번호 형식이 맞지 않는다면...
if (!tel2.match(patternTel)) {
}

// 전화번호가 숫자가 들어가져 있는지 체크
if (!patternNum.test(frm.pw.value)) {
}
