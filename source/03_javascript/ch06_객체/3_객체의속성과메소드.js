let name = '이순신';
let methid = function (i) {
  console.log(1);
};
let person = {
  name: '이순신',
  age: 20,
  // eat 함수는 화살표 함수를 쓰면 안 된다.
  eat: function (food) {
    // 메소드 내에서는 this 키워드 사용
    let msg = `${this.age} 살 ${this.name} 님은 ${food} 를 먹는다.`;
    console.log(msg);
  }, // eat 함수
};

console.log(`${person.name} 님 ${person.age} 살`);
console.log(person);
console.log(person.toString()); // person.toString() 은 person를 웹에서 document.write(person) 같다.
person.eat('불고기');
