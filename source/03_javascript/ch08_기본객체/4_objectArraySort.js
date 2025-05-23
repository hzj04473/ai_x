function Student(name, kor, mat, eng, sci) {
  this.name = name;
  this.kor = kor;
  this.mat = mat;
}

// Student 타입의 함수를 ptototype에 추가
Student.prototype.getSum = function () {
  return this.kor + this.mat;
};
Student.prototype.toString = function () {
  let outPut = '';
  for (let key in this) {
    if (key !== 'toString' && key !== 'getSum') {
      outPut += `${key} : ${this[key]} `;
    } else if (key === 'getSum') {
      // ${key.substring(3)} 은 Sum
      outPut += `${key.substring(3).toLowerCase()} : ${this[key]()} `;
    }
  }
  return outPut;
};

let students = [];

students.push(new Student('김길동', 79, 99));
students.push(new Student('홍길동', 99, 99));
students.push(new Student('신길동', 39, 49));
students.push(new Student('유길동', 89, 29));
students.push(new Student('박길동', 79, 89));

console.log(`정렬전`);
students.forEach((data, idx) => console.log(`${idx} : ${data}`));

students.sort(); // 문자로 변환 후 ascii코드 정렬

console.log(`정렬후(ascii코드 정렬)`);
students.forEach((data, idx) => console.log(`${idx} : ${data}`));

students.sort((left, right) => right.getSum() - left.getSum()); //총점 기준 내림차순 정렬
console.log(`총점 기준 내림차순 정렬`);
students.forEach((data, idx) => console.log(`${idx} : ${data}`));

// 수학점수 기준 오른차순 정렬
students.sort((left, right) => left.mat - right.mat); // 수학점수 기준 오른차순 정렬
console.log(`수학점수 기준 오른차순 정렬`);
students.forEach((data, idx) => console.log(`${idx} : ${data}`));
