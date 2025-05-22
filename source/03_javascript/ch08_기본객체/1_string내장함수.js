var str = 'Abc@Abcd@'; // ['A','b','c','@','A','b','c','d','@']
console.log(`원본 : ${str}`);
console.log(`글자길이 : ${str.length}`);
console.log(`첫번쨰글자 : ${str[0]}`);
console.log(`글자연결 : ${str.concat(str)}`);

// str.substring(a, b) a번째부터 b번째 앞까지 추출
// str.substring(a) a번째부터 끝까지 추출z
// str.substr(a,b) a번째부터 글자 b글자 추출
console.log(`3번째부터 7번쨰 글자 추출 : ${str.substring(3, 8)} `);
console.log(`3번째부터 끝가지 글자 추출 : ${str.substring(3)} `);
console.log(`5번째부터 글자 3글자 추출 : ${str.substr(5, 3)}`);
console.log(`맨처음 나오는 @의 위치 : ${str.indexOf('@')}`);
console.log(`맨마지막 나오는 @의 위치 : ${str.lastIndexOf('@')}`);
console.log(`양쪽 space 없애기 : ${'   my app   '.trim()}`);
console.log(`대문자로 전환 : ${str.toUpperCase()}`);
console.log(`소문자로 전환 : ${str.toLowerCase()}`);
console.log(`@ 를 - 로 전환(처음) : ${str.replace('@', ' - ')}`);
console.log(`@ 를 - 로 전환(모두) : ${str.replaceAll('@', ' - ')}`);
console.log(`@ 업애기 : ${str.replaceAll('@', '')}`);
console.log(`원본 : ${str}`);
