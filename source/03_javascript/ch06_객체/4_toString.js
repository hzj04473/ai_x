let person = {
  name: '이순신',
  age: 20,
  // eat 함수는 화살표 함수를 쓰면 안 된다.
  eat: function (food) {
    // 메소드 내에서는 this 키워드 사용
    let msg = `${this.age} 살 ${this.name} 님은 ${food} 를 먹는다.`;
    alert(msg);
  }, // eat 함수
  toString: function () {
    let outPut = ''; // toString함수가 return 할 문자
    for (let key in this) {
      if (key !== 'eat' && key !== 'toString') {
        // outPut = `${outPut} ${key} : ${this[key]}<br />`;
        outPut += `${key} : ${this[key]}<br />`;
      }
    }

    return outPut;
  }, // toString 함수 파이썬에서의 __str__역할
};
