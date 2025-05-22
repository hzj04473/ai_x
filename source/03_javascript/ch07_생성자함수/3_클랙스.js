class Student {
  constructor(name, kor, mat, eng, sci) {
    this.name = name;
    this.kor = kor;
    this.mat = mat;
    this.eng = eng;
    this.sci = sci;
  }
  getSum() {
    return this.kor + this.mat + this.eng + this.sci;
  }
  getAvg() {
    return this.getSum() / 4;
  }

  toString() {
    return `name: ${this.name} kor: ${this.kor} mat: ${this.mat} eng: ${this.eng} sci: ${this.sci} sum: ${this.getSum()} avg: ${this.getAvg()}`;
  }
}

let hong = new Student('홍', 99, 99, 99, 99);
console.log(hong.toString());
console.log(`${hong}`);
console.log(hong);

// let student = [];
// student.push(new Student('홍', 99, 99, 99, 99));
// student.push(new Student('김', 91, 95, 99, 99));
// student.push(new Student('백', 99, 99, 99, 19));
// student.forEach((data, idx) => console.log(`${idx} : ${data}\n`));
