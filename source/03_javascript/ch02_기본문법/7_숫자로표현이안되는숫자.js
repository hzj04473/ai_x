i = Number('');
console.log(`i = ${i} => 타입 = ${typeof i}`); // 0
i = parseInt(''); // NaN
console.log(`i = ${i} => 타입 = ${typeof i}`); // NaN

f = 10 / 3;
console.log(`f = ${f} => 타입 = ${typeof f}`);

a = 10 / 0; // 10 / 0.00000000000000000000000000000001
console.log(`a = ${a} => 타입 = ${typeof a}`);

console.log(`i 가 NaN 인지 여부 : ${isNaN(i)}`); // true
console.log(`f 가 NaN 인지 여부 : ${isNaN(f)}`); // false

console.log(`a 가 유한수인지 여부 : ${isFinite(a)}`); // false
console.log(`f 가 유한수인지 여부 : ${isFinite(f)}`); // true
