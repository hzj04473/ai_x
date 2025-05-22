/**
 *
 * Python 에서 객체
 *
 * class Person:
 *  def __init__(self, name, age):
 *    self.name = name
 *    self.age = age
 *
 *  def eat(self, food):
 *    print(self.name + '이' + food +' 를 먹는다.')
 *
 *  def __str__():
 *    return self.name + self.age
 *
 * p = Person('홍길동',20)
 * print(person)
 * print(person.name, person.age)
 * person.eat('물고기')
 *
 */

const person = { name: '홍길동', age: 20 };
console.log('person 객체 출력1 : ' + person['name'], person['age']);
console.log('person 객체 출력2 : ' + person.name, person.age);

const arr = ['홍길동', 20]; // {0:홍길동, 1:20}
console.log('arr 배열 출력: ' + arr[0], arr[1]);
