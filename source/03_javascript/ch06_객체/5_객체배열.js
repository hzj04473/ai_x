let students = [
  { name: '홍', kor: 99, mat: 90, eng: 99, sci: 99 },
  { name: '김', kor: 99, mat: 90, eng: 80, sci: 99 },
];

students.push({ name: '이', kor: 99, mat: 90, eng: 70, sci: 99 });

for (let idx in students) {
  // getSum() 함수 추가
  students[idx].getSum = function () {
    return this.kor + this.mat + this.eng + this.sci;
  };

  // getAvg() 함수 추가
  students[idx].getAvg = function () {
    return this.getSum() / 4;
  };

  // toString() 함수 정의
  students[idx].toString = function () {
    let outPut = '';
    for (let key in this) {
      if (key !== 'toString' && key !== 'getSum' && key !== 'getAvg') {
        outPut += `${key} : ${this[key]} `;
      } else if (key === 'getSum') {
        // ${key.substring(3)} 은 Sum
        outPut += `${key.substring(3)} : ${this[key]()} `;
      } else if (key === 'getAvg') {
        // ${key.substring(3)} 은 Avg
        outPut += `${key.substring(3)} : ${this[key]()} \n`;
      }
    }
    return outPut;
  };
}

var out = ''; //alert 함수에 출려한 문자를 담을 변수
for (let idx = 0; idx < students.length; idx++) {
  out += students[idx];
}
