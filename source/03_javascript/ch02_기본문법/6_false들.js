// false 로 간주되는 값 : undefined => 0 => NaN => '' => null
// Boolean(값) : boolean 으로 형변환
// Number(값) : number 으로 형변환
// String(값) : string 으로 형변환

var i;

console.log(`${i} => ${Boolean(i)}`); // fasle
console.log(`0 => ${Boolean(0)}`); // fasle
console.log(`NaN => ${Boolean(NaN)}`); // fasle
console.log(`Number('a') => ${Boolean(Number('a'))}`); // fasle
console.log(`'' => ${Boolean('')}`); // fasle
console.log(`' ' => ${Boolean(' ')}`); // true
console.log(`null => ${Boolean(null)}`); // fasle
